#  Honeypot script, scanning Zeek logs to find POST requests on wp-admin vulnerable form  #
#  Made by Arkadskov Arseniy, Motin Danila and Bobrov Ilya, KTSO-02-20. #

# Script must be ran in the same directory as rule.yara
# Also root user required for this script to run properly

import subprocess
import os
import pyfiglet

print(pyfiglet.figlet_format("Gachi honeypot"))

rootCheck = str(subprocess.run(["whoami"], capture_output = True))

choice = "N"

if "root" in rootCheck:
    print("Scanning...")

    while(True):
        status = str(subprocess.run(["yara", "rule.yara", "/opt/zeek/logs/current"], capture_output = True))
        if "meterpreter" in status:
            print("Compromise detected!")
            choice = input("Going to kill all www-data processes. Proceed?[Y/N]")
            if(choice == "Y"):
                os.system("sudo killall --user www-data")
                print("Done!")
                break
            else:
                print("Exiting...")
                break
        else:
            print("No suspicious activity found")
            os.system("sleep 5")
else:
    print("Not a root user! Please use sudo to run this script.")