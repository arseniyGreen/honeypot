import os

print("Init scanner")

while(1):
    output = os.system("yara meterpreter.yar /var/www")
    print(output)