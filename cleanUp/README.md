# cleanUp Directory

This folder contains the Python scripts used to list and filter AWS EBS volumes that are not referenced by Kubernetes Persistent Volumes.  Each script performs a small task so they can be combined from `main.py`.

## Files

- **main.py** – entry point that orchestrates the workflow and handles command line arguments.
- **aws_extract.py** – retrieves EBS volume information from AWS.
- **pv_extract.py** – gets the names of Persistent Volumes from the Kubernetes cluster.
- **process_volume.py** – combines AWS and Kubernetes data to find volumes without matching PVs.
- **printout.py** – formats the final list of volumes for display.
- **validate_args.py** – validates command line options for the main script.
- **kp.py / nkp.py** – filter volumes based on presence or absence of the Karpenter tag.
- **pv.py / npv.py** – filter volumes based on the PV tag.
- **cluster.py / ncluster.py** – filter volumes created by the CSI driver or not.
- **preflight.py** – performs environment checks before running the other scripts.

Run `./main.py --help` for usage details.
