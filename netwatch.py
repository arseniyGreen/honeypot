import os

print("Scanning...")

while(1):
    status = os.system("netstat | grep 4444")

    if(status == 256):
        print("No suspicious activity found")
        os.system("sleep 7")
    else:
        print("We've been hacked!")
        os.system("Sleep 4")