#!/bin/python3

import boto3
import warnings

# Suppress the specific PythonDeprecationWarning from boto3
from boto3.compat import PythonDeprecationWarning
warnings.filterwarnings("ignore", category=PythonDeprecationWarning)

def list_all_ebs_volumes(region_name='us-east-1'):
    """
    Retrieve all EBS volumes with their Name, Volume ID, 'kubernetes.io/created-for/pv/name' tag, 
    'karpenterProvisionerName' tag, and 'ebs.csi.aws.com/cluster' tag.

    Args:
    region_name (str): AWS region to query.

    Returns:
    list: A list of tuples containing EBS volume Name, Volume ID, PV tag, KP tag, and Cluster tag.
    """
    # Initialize the EC2 client
    ec2 = boto3.client('ec2', region_name=region_name)

    # Retrieve all EBS volumes
    volumes = ec2.describe_volumes()

    # Extract required details
    volume_details = []
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        name_tag = "NoName"
        pv_tag = "NoPV"
        kp_tag = "NotKP"
        cluster_tag = "NotCluster"

        # Check for tags
        if 'Tags' in volume:
            for tag in volume['Tags']:
                if tag['Key'] == 'Name':
                    name_tag = tag['Value']
                elif tag['Key'] == 'kubernetes.io/created-for/pv/name':
                    pv_tag = tag['Value']
                elif tag['Key'] == 'karpenterProvisionerName':
                    kp_tag = tag['Value']
                elif tag['Key'] == 'ebs.csi.aws.com/cluster' and tag['Value'] == 'true':
                    cluster_tag = "Cluster"

        # Append details with default values for missing tags
        volume_details.append((name_tag, volume_id, pv_tag, kp_tag, cluster_tag))

    return volume_details

if __name__ == '__main__':
    volumes = list_all_ebs_volumes()
    for volume in volumes:
        print(f"Name: {volume[0]} Vol-ID: {volume[1]} PV: {volume[2]} KP: {volume[3]} Cluster: {volume[4]}")

