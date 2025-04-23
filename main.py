#!/usr/bin/env python3
import subprocess
import os
import logging



def check_service_status(service_name):
    if subprocess.call(['systemctl', 'is-active', '--quiet', service_name]) == 0:
        logging.info(f"{service_name} is running.")
        print(f"{service_name} is running.")
        return True
    else:
        print(f"{service_name} is starting.")
        logging.info(f"{service_name} is not running.")
        subprocess.call(['systemctl', 'start', service_name])
        logging.info(f"{service_name} started.")
        return False
    
        if subprocess.call(['systemctl', 'is-active', '--quiet', service_name]) == 0:
            return True
        else:
            logging.warning(f"{service_name} failed to start.")
            return False          
userInput = input("Enter the service name to check: ")
check_service_status(userInput)

       

  


