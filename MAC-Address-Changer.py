#MAC Address Changer for Linux system
#from Udemy course "Learn Python and Ethical Hacking From Scratch"
#fleshed out with user input (if/else and MAC address input)

#Quick run-down on the bash commands for manual config:
#
#root@kali:~# ifconfig eth0 down
#root@kali:~# ifconfig eth0 hw ether xx:xx:xx:xx:xx:xx
#root@kali:~# ifconfig eth0 up

# note to self: subprocess allows execution of commands on native OS terminal
# first attempt Linux

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

#second attempt for Linux - using parsing, decisions and functions
#sanitisation of user input is also included
#!declaration! - this is not my own code!! in this case, for this attempt, i'm just running through the course content as practice.

import subprocess
import optparse

def run_parser():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("interface invalid, use --help for more information")
    elif not options.newMac:
        parser.error("MAC invalid, use --help for more information")
    return options

def set_mac(interface, newMac):
    print("changing " + interface + " to " + newMac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up"])

options = run_parser()
set_mac(options.interface, options.newMac)

#!end!
    
# first attempt for windows (might work - currently have no test environment - once i have a Windows VM i can destroy without consequence, i'll try it out.):

import subprocess

subprocess.run("powershell.exe -command Get-NetAdapter", shell=True)
#subprocess.run("PowerShell.exe","Get-NetAdapter", shell=True)

interface = input("enter interface you wish to change: ")
usrSelection = input ("do you want to change you MAC address for " + interface + " y/n: ")

if usrSelection == "y":
    newMac = input ("enter new MAC address. format xx:xx:xx:xx:xx:xx: ")
    psCommand1 = "Disable-NetAdapter -Name " + interface
    psCommand2 = "Set-NetAdapter -Name " + interface + " -MacAddress " + newMac
    psCommand3 = "Enable-NetAdapter -Name " + interface
    subprocess.call("powershell.exe -command " + psCommand1 , shell=True)
    subprocess.call("powershell.exe -command " + psCommand2 , shell=True)
    subprocess.call("powershell.exe -command " + psCommand3 , shell=True)
        
else:
    print("MAC address not changed")

#Second attempt for Windows : running Powershell script through python
#I've tried various ways, can't seem to get it to run just yet. I'll come back to this one at a later date
#I can imagine something like this, piggybacking scripts through scripts, could be very important later on
#
#the PowerShell Script can be found in my PowerShell projects file
#
#PowerShell script that might work (currently have no test environment):
#

import subprocess

psScript = "C:\Users\dslew\OneDrive\Documents\GitHub\PowerShell-Projects\Mac-Changer-PS.ps1"
psCommand = "powershell.exe -file " + psScript 

subprocess.run(psCommand, shell=True)

