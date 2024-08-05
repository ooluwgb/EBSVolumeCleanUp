#!/bin/python3

import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Argument validation script.",
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
    parser.add_argument('--npv', action='store_true', help="Extract and print the PVs and volume IDs.")
    parser.add_argument('--cluster', action='store_true', help="Extract and print the cluster attribute.")
    parser.add_argument('--ncluster', action='store_true', help="Extract and print the cluster attribute.")
    parser.add_argument('--kp', action='store_true', help="Extract and print the KP attribute.")
    parser.add_argument('--nkp', action='store_true', help="Extract and print the KP attribute.")
    return parser.parse_args()

def validate_arguments(args):
    errors = []
    
    if args.pv and args.npv:
        errors.append("Error: --pv and --npv are opposite tags and cannot be used together.")
    if args.cluster and args.ncluster:
        errors.append("Error: --cluster and --ncluster are opposite tags and cannot be used together.")
    if args.kp and args.nkp:
        errors.append("Error: --kp and --nkp are opposite tags and cannot be used together.")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print("\nUsage:", file=sys.stderr)
        print("  ./main.py [OPTIONS]", file=sys.stderr)
        print("\nOptions:", file=sys.stderr)
        print("  --id              Print the volume IDs.", file=sys.stderr)
        print("  --name            Extract and print the names and volume IDs.", file=sys.stderr)
        print("  --pv              Extract and print the PVs and volume IDs.", file=sys.stderr)
        print("  --npv             Extract and print the PVs and volume IDs.", file=sys.stderr)
        print("  --cluster         Extract and print the cluster attribute.", file=sys.stderr)
        print("  --ncluster        Extract and print the cluster attribute.", file=sys.stderr)
        print("  --kp              Extract and print the KP attribute.", file=sys.stderr)
        print("  --nkp             Extract and print the KP attribute.", file=sys.stderr)
        sys.exit(1)
    else:
        return args

if __name__ == '__main__':
    args = parse_arguments()
    validate_arguments(args)
    
    # Print the validated arguments to be used by main.py
    if any(vars(args).values()):
        print(" ".join(sys.argv[1:]))

