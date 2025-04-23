#!/usr/bin/env python3
import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename='service_check.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Function to check if a service is installed
def is_service_installed(service_name):
    result = subprocess.run(
        ['systemctl', 'status', service_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode != 4  # code 4 means 'unit not found'

# Function to check and start service if not running
def check_service_status(service_name):
    if subprocess.call(['systemctl', 'is-active', '--quiet', service_name]) == 0:
        logging.info(f"{service_name} is running.")
        print(f"{service_name} is running.")
        return True
    else:
        logging.warning(f"{service_name} is not running.")
        print(f"{service_name} is not running. Attempting to start it...")
        subprocess.call(['sudo', 'systemctl', 'start', service_name])
        logging.info(f"{service_name} start attempted.")

        # Check again after trying to start
        if subprocess.call(['systemctl', 'is-active', '--quiet', service_name]) == 0:
            logging.info(f"{service_name} started successfully.")
            print(f"{service_name} started successfully.")
            return True
        else:
            logging.error(f"{service_name} failed to start.")
            print(f"{service_name} failed to start.")
            return False

# Get user input
userInput = input("Enter the service name to check: ").strip()

# Main logic
if not is_service_installed(userInput):
    print(f"The service '{userInput}' is not installed. Attempting to install...")
    logging.info(f"{userInput} not installed. Installing...")
    subprocess.run(['sudo', 'apt', 'install', '-y', userInput])
    logging.info(f"{userInput} installation attempted.")
else:
    check_service_status(userInput)
