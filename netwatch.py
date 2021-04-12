import os

print("Scanning...")

choice = "n"
run = True

while(run):
    status = os.system("netstat | grep 4444")

    if(status == 256):
        print("No suspicious activity found")
        os.system("sleep 7")
    else:
        print("We've been hacked!")
        print("Going to kill all www-data processes. Continue? [y/n]")
        choice = input()
        if(choice == "y"):
            os.system("sudo killall --user www-data")
            if(os.system("sudo killall --user www-data") == 0):
                print("Success!")
                break
            else:
                print("Error occured!")
                break
        elif(choice == "n"):
            print("Exiting...")
            break
        else:
            print("Invalid input!")
            break