# Script must be ran in the same directory as rule.yara

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