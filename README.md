# EBSVolumeCleanUp

This repository provides a script for identifying and cleaning up orphaned Amazon Elastic Block Store (EBS) volumes in an AWS environment. The script compares EBS volumes in AWS with Persistent Volumes (PV) in an Amazon Elastic Kubernetes Service (EKS) cluster to find and delete volumes that are no longer associated with any resources, thus helping to reduce unnecessary costs.

## Key Features of the Script
- **Identification of Orphaned Volumes:** The script lists EBS volumes that are not attached to any EC2 instances or persistent volumes in an EKS cluster.
- **Customizable Filters:** Users can specify various arguments to filter EBS volumes based on criteria such as volume type, size, or specific tags.
- **Automated Cleanup:** The script automates the deletion of identified orphaned volumes, ensuring that AWS resources are optimized and costs are controlled.

## Requirements
To use this script, the following prerequisites must be met:
- **AWS Credentials:** Authentication credentials for AWS cloud services must be configured on the system where the script is running. This is essential for the script to access and manage AWS resources.
- **Kubernetes Configuration:** The Kubernetes control plane must be configured, allowing the script to interact with the EKS cluster.
- **Environment Compatibility:** The script is designed to work in a Python environment on a Linux system, specifically on Debian-based distributions. Proper Python packages and dependencies should be installed.

## Running the Script
The script can be executed with various command-line arguments. Using the `--help` flag provides detailed instructions on available options and how to use them effectively.

For more details and to access the code, visit the [EBSVolumeCleanUp GitHub repository](https://github.com/ooluwgb/EBSVolumeCleanUp).
