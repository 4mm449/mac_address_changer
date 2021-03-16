#!/usr/bin/env/python
#VERSION 2 DATED 16TH MARCH 2021
import subprocess
import optparse
import re
#Function to get arguments and parse it
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The MAC address you want to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAc address, use --help for more info")
    return options
#Function to get the interface and new MAC address
def change_mac(interface, new_mac):
    # print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    # print("[+] MAC address changed to " + new_mac)
#Function to print ifconfig interface MAC address
def print_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])

    mac_address_filtered = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_filtered:
        return mac_address_filtered.group(0)
    else:
        print("[-] Could not read the MAC Address")

options = get_arguments() #arguments
current_mac = print_mac(options.interface)
print("Previous MAC> " + str(current_mac)) #print filtered ifconfig result
change_mac(options.interface, options.new_mac) #get new mac and int

current_mac = print_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC Address Changed to " + current_mac)
else:
    print("MAC address could not be changed")
print("New MAC> " + str(current_mac)) #print changed mac
