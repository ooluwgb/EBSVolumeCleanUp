#!/bin/python3

import json
import subprocess

def get_pv_names():
    """
    Retrieve the names of all PVs in the Kubernetes cluster.

    Returns:
    list: A list of PV names.
    """
    # Run kubectl command to get PVs in JSON format
    result = subprocess.run(['kubectl', 'get', 'pv', '-o', 'json'], stdout=subprocess.PIPE, check=True)
    pvs = json.loads(result.stdout)

    # Process the JSON output to extract PV names
    pv_names = [pv['metadata']['name'] for pv in pvs['items']]

    return pv_names

if __name__ == '__main__':
    pv_names = get_pv_names()
    for pv_name in pv_names:
        print(pv_name)

