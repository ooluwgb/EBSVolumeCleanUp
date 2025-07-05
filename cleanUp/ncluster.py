#!/usr/bin/env python3

import sys
import json

def filter_ncluster(data):
    """
    Filter out all volumes with the attribute Cluster: Cluster.

    Args:
    data (list): The data to process.

    Returns:
    list: The filtered data.
    """
    filtered_data = [item for item in data if item[4] != "Cluster"]
    return filtered_data

if __name__ == '__main__':
    # Read data from stdin
    input_data = sys.stdin.read()
    data = json.loads(input_data)

    # Filter data
    filtered_data = filter_ncluster(data)

    # Output filtered data as JSON
    print(json.dumps(filtered_data))

