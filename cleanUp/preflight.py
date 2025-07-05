#!/usr/bin/env python3
"""Pre-flight checks for the cleanup scripts."""

import shutil
import subprocess
import sys
import os

import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def command_exists(cmd):
    """Return True if a command exists on PATH."""
    return shutil.which(cmd) is not None


def check_python_version():
    if sys.version_info.major < 3:
        sys.exit("Python 3 is required to run this script")


def check_command(cmd):
    if not command_exists(cmd):
        sys.exit(f"Required command '{cmd}' not found in PATH")


def check_aws_credentials():
    try:
        boto3.client("sts").get_caller_identity()
    except NoCredentialsError:
        sys.exit("AWS credentials not found. Configure a profile before running.")
    except ClientError as exc:
        sys.exit(f"Unable to validate AWS credentials: {exc}")


def check_kube_config():
    kubeconfig = os.environ.get("KUBECONFIG", os.path.expanduser("~/.kube/config"))
    if not os.path.exists(kubeconfig):
        sys.exit("Kubernetes configuration not found. Ensure kubectl is configured.")
    try:
        subprocess.run(["kubectl", "version", "--client"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (OSError, subprocess.CalledProcessError) as exc:
        sys.exit(f"kubectl is not configured correctly: {exc}")


def run_checks():
    """Run all pre-flight checks."""
    check_python_version()
    check_command("aws")
    check_command("kubectl")
    check_aws_credentials()
    check_kube_config()


if __name__ == "__main__":
    run_checks()
    print("Environment looks good.")
