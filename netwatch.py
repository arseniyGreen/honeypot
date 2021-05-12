# Script must be ran in the same directory as rule.yara

import subprocess
import os
import pyfiglet

print(pyfiglet.figlet_format("Gachi honeypot"))

print("Scanning...")

choice = "N"

while(True):
    status = str(subprocess.run(["yara", "rule.yara", "/opt/zeek/logs/current"]))
    if "meterpreter" in status:
        print("Compromise detected!")
        choice = input("Going to kill all www-data processes. Proceed?[Y/N]")
        if(choice == "Y"):
            os.system("sudo killall --user www-data")
            print("Done!")
        else:
            print("Exiting...")
            break
    else:
        print("No suspicious activity found")
        os.system("sleep 5")