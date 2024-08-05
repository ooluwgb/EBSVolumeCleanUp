#!/bin/python3

import argparse
import sys
import json

def extract_attributes(data, args):
    for name, vol_id, pv, kp, cluster in data:
        output = f"Vol-ID: {vol_id}"
        if args.name:
            output += f" Name: {name}"
        if args.pv or args.npv:
            output += f" PV: {pv}"
        if args.cluster or args.ncluster:
            output += f" Cluster: {cluster}"
        if args.kp or args.nkp:
            output += f" KP: {kp}"
        print(output)

def print_ids(data):
    for _, vol_id, _, _, _ in data:
        print(f"Vol-ID: {vol_id}")

def print_raw_data(data):
    for name, vol_id, pv, kp, cluster in data:
        print(f"Vol-ID: {vol_id} Name: {name} PV: {pv} KP: {kp} Cluster: {cluster}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Printout script to process EBS volumes.")
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
    if args.pv and args.npv:
        print("Error: --pv and --npv are opposite tags and cannot be used together.")
        sys.exit(1)
    if args.cluster and args.ncluster:
        print("Error: --cluster and --ncluster are opposite tags and cannot be used together.")
        sys.exit(1)
    if args.kp and args.nkp:
        print("Error: --kp and --nkp are opposite tags and cannot be used together.")
        sys.exit(1)

if __name__ == '__main__':
    args = parse_arguments()
    validate_arguments(args)

    # Read data from stdin
    input_data = sys.stdin.read()
    data = json.loads(input_data)

    if not data:
        print("No volumes found in the latest state.")
        sys.exit(0)

    if args.id and not any([args.name, args.pv, args.npv, args.cluster, args.ncluster, args.kp, args.nkp]):
        print_ids(data)
    elif any([args.name, args.pv, args.npv, args.cluster, args.ncluster, args.kp, args.nkp]):
        extract_attributes(data, args)
    else:
        print_raw_data(data)

