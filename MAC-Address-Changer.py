﻿#MAC Address Changer for Linux system
#from Udemy course "Learn Python and Ethical Hacking From Scratch"

#Quick run-down on the bash commands for manual config:
#
#root@kali:~# ifconfig eth0 down
#root@kali:~# ifconfig eth0 hw ether xx:xx:xx:xx:xx:xx
#root@kali:~# ifconfig eth0 up

# not to self: subprocess allows execution of commands on native OS terminal

import subprocess

subprocess.call("ifconfig", shell=True)
usrSelection = input ("do you want to change you MAC address for eth0? y/n: ")

if usrSelection == "y":
    subprocess.call("ifconfig eth0 down", shell=True)
    newMac = input ("enter new MAC address. format xx:xx:xx:xx:xx:xx: ")
    subprocess.call("ifconfig eth0 hw ether" + newMac, shell=True)
    subprocess.call("ifconfig eth0 up", shell=True)
    
else:
    print("MAC address not changed")
    



