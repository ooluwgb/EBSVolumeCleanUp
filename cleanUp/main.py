#!/usr/bin/env python3

import subprocess
import sys
import json
import os
import argparse
from process_volume import find_unmatched_volumes
from preflight import run_checks

# Determine the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name, data):
    """
    Run a script to filter the data.

    Args:
    script_name (str): The script to run.
    data (list): The data to process.

    Returns:
    list: The filtered data.
    """
    script_path = os.path.join(script_dir, script_name)
    result = subprocess.run([sys.executable, script_path], input=json.dumps(data), universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running {script_name}")
        print(result.stderr)
        sys.exit(1)
    return json.loads(result.stdout)

def parse_main_arguments():
    parser = argparse.ArgumentParser(
        description="Main script to process EBS volumes.",
        epilog="Example usage:\n"
               "  ./main.py --id\n"
               "  ./main.py --name\n"
               "  ./main.py --pv\n"
               "  ./main.py --npv\n"
               "  ./main.py --cluster\n"
               "  ./main.py --ncluster\n"
               "  ./main.py --kp\n"
               "  ./main.py --nkp\n"
               "  ./main.py --name --pv\n"
               "  ./main.py --name --nkp\n"
               "  ./main.py --kp --cluster\n"
               "  ./main.py --name --cluster --nkp --pv",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--id', action='store_true', help="Print the volume IDs.")
    parser.add_argument('--name', action='store_true', help="Extract and print the names and volume IDs.")
    parser.add_argument('--pv', action='store_true', help="Extract and print the PVs and volume IDs.")
    parser.add_argument('--npv', action='store_true', help="Extract, filter out volumes without PV, and print the PVs and volume IDs.")
    parser.add_argument('--cluster', action='store_true', help="Extract and print the cluster attribute.")
    parser.add_argument('--ncluster', action='store_true', help="Extract, filter volumes not created by aws.ebs.csi, and print the cluster attribute.")
    parser.add_argument('--kp', action='store_true', help="Extract and print the KP attribute.")
    parser.add_argument('--nkp', action='store_true', help="Extract, filter volumes not created by Karpenter, and print the KP attribute.")
    return parser

if __name__ == '__main__':
    run_checks()
    # Parse and validate arguments
    parser = parse_main_arguments()
    args = parser.parse_args()

    if not any(vars(args).values()):
        print("No arguments passed. Running the default script.")
        state = find_unmatched_volumes()
    else:
        # Validate arguments
        validation_script = os.path.join(script_dir, 'validate_args.py')
        validation_result = subprocess.run([sys.executable, validation_script] + sys.argv[1:], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if validation_result.returncode != 0:
            print("Error validating arguments:")
            print(validation_result.stderr)
            sys.exit(1)

        # Extract the validated arguments
        validated_args = validation_result.stdout.strip().split()
        state = find_unmatched_volumes()

        if '--cluster' in validated_args:
            state = run_script('cluster.py', state)
        if '--ncluster' in validated_args:
            state = run_script('ncluster.py', state)
        if '--kp' in validated_args:
            state = run_script('kp.py', state)
        if '--nkp' in validated_args:
            state = run_script('nkp.py', state)
        if '--pv' in validated_args:
            state = run_script('pv.py', state)
        if '--npv' in validated_args:
            state = run_script('npv.py', state)

    # Always pass the state to the printout script
    printout_script = os.path.join(script_dir, 'printout.py')
    printout_result = subprocess.run([sys.executable, printout_script] + sys.argv[1:], input=json.dumps(state), universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if printout_result.returncode != 0:
        print("Error running printout.py")
        print(printout_result.stderr)
        sys.exit(1)
    print(printout_result.stdout)

