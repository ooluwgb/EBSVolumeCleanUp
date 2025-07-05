#!/usr/bin/env python3

import sys
import json

def filter_kp(data):
    """
    Filter out all volumes with the attribute KP: NotKP.

    Args:
    data (list): The data to process.

    Returns:
    list: The filtered data.
    """
    filtered_data = [item for item in data if item[3] != "NotKP"]
    return filtered_data

if __name__ == '__main__':
    # Read data from stdin
    input_data = sys.stdin.read()
    data = json.loads(input_data)

    # Filter data
    filtered_data = filter_kp(data)

    # Output filtered data as JSON
    print(json.dumps(filtered_data))

