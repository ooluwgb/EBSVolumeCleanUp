#!/bin/python3

import sys
import os
from aws_extract import list_all_ebs_volumes
from pv_extract import get_pv_names

def find_unmatched_volumes():
    """
    Retrieve and filter AWS EBS volumes that are not matched with Kubernetes PVs.

    Returns:
    list: A list of tuples containing unmatched AWS volume details.
    """
    # Get all EBS volumes from AWS with their details
    aws_volumes = list_all_ebs_volumes()

    # Get PV names from the Kubernetes cluster
    pv_names = get_pv_names()

    # Find unmatched volumes
    unmatched_volumes = [
        (name, vol_id, pv, kp, cluster)
        for name, vol_id, pv, kp, cluster in aws_volumes
        if pv == "NoPV" or pv not in pv_names
    ]

    return unmatched_volumes

def print_volumes(volumes):
    """
    Print the details of the unmatched volumes.

    Args:
    volumes (list): List of volumes.
    """
    for name, vol_id, pv, kp, cluster in volumes:
        print(f"Vol-ID: {vol_id} Name: {name} PV: {pv} KP: {kp} Cluster: {cluster}")

if __name__ == '__main__':
    # Find unmatched volumes
    unmatched_volumes = find_unmatched_volumes()

    # Print the filtered results
    print_volumes(unmatched_volumes)

