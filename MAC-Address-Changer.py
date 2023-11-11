#MAC Address Changer for Linux system
#from Udemy course "Learn Python and Ethical Hacking From Scratch"
#fleshed out with user input (if/else and MAC address input)

#Quick run-down on the bash commands for manual config:
#
#root@kali:~# ifconfig eth0 down
#root@kali:~# ifconfig eth0 hw ether xx:xx:xx:xx:xx:xx
#root@kali:~# ifconfig eth0 up

# note to self: subprocess allows execution of commands on native OS terminal

import subprocess

subprocess.call("ifconfig", shell=True)

interface = input("enter interface you wish to change: ")
usrSelection = input ("do you want to change you MAC address for " + interface + " y/n: ")

if usrSelection == "y":
    subprocess.call("ifconfig " + interface + " down", shell=True)
    newMac = input ("enter new MAC address. format xx:xx:xx:xx:xx:xx: ")
    subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    
else:
    print("MAC address not changed")
    
