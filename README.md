# EBSVolumeCleanUp

This repository provides a set of Python scripts for identifying orphaned Amazon Elastic Block Store (EBS) volumes.  The workflow compares EBS volumes in AWS with Persistent Volumes (PV) in an Amazon Elastic Kubernetes Service (EKS) cluster to highlight volumes that are not referenced by Kubernetes.  Deletion is intentionally left as a manual step so you can review the output before removing resources.

## Key Features of the Script
- **Identification of Orphaned Volumes:** The script lists EBS volumes that are not attached to any EC2 instances or persistent volumes in an EKS cluster.
- **Customizable Filters:** Users can specify various arguments to filter EBS volumes based on criteria such as volume type, size, or specific tags.
- **Pre‑flight Checks:** `main.py` verifies that Python 3, `aws` and `kubectl` are available and that AWS credentials and Kubernetes config are set up before running.

## Requirements
To use this script, the following prerequisites must be met:
- **AWS Credentials:** Authentication credentials for AWS cloud services must be configured on the system where the script is running. This is essential for the script to access and manage AWS resources.
- **Kubernetes Configuration:** The Kubernetes control plane must be configured, allowing the script to interact with the EKS cluster.
- **Environment Compatibility:** The script is designed to work in a Python environment on a Linux system, specifically on Debian-based distributions. Proper Python packages and dependencies should be installed.

## Running the Script
The script can be executed with various command-line arguments. Using the `--help` flag provides detailed instructions on available options and how to use them effectively.

See [cleanUp/README.md](cleanUp/README.md) for a description of the individual scripts.

For more details and to access the code, visit the [EBSVolumeCleanUp GitHub repository](https://github.com/ooluwgb/EBSVolumeCleanUp).
