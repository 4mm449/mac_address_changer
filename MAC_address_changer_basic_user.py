#!/usr/bin/env python
import subprocess
import re
print('''
##     ##    ###     ######           ######  ##     ##    ###    ##    ##  ######   ######## ########  
###   ###   ## ##   ##    ##         ##    ## ##     ##   ## ##   ###   ## ##    ##  ##       ##     ## 
#### ####  ##   ##  ##               ##       ##     ##  ##   ##  ####  ## ##        ##       ##     ## 
## ### ## ##     ## ##       ####### ##       ######### ##     ## ## ## ## ##   #### ######   ########  
##     ## ######### ##               ##       ##     ## ######### ##  #### ##    ##  ##       ##   ##   
##     ## ##     ## ##    ##         ##    ## ##     ## ##     ## ##   ### ##    ##  ##       ##    ##  
##     ## ##     ##  ######           ######  ##     ## ##     ## ##    ##  ######   ######## ##     ## 


''')
input("This Program was created by Ammaar on March 28th 2020.\n""Last updated on March 11th 2021\n""Latest version is v2.0. This is v2.0\n" "Use this program with caution. Press Enter (Return) to continue... ")
int_list = subprocess.call("ifconfig")
input("After you click enter, you will be required to choose an interface, you can choose one from the list above. Press Enter (Return) to continue...")

interface = input("Please Specify The Name Of The Interface That You would Like To Change The MAC Address For\n")
new_mac_address = input("Please Enter The MAC Address That You Would Like To Change To\n")
subprocess.call("sudo ifconfig "+interface+" down", shell=True)
subprocess.call("sudo ifconfig "+interface +" hw ether "+new_mac_address, shell=True)
subprocess.call("sudo ifconfig "+interface+" up ", shell=True)

# subprocess.call(["sudo ifconfig", interface, "down"])
# subprocess.call(["sudo ifconfig", interface, "hw ether", new_mac_address])
# subprocess.call(["sudo ifconfig", interface, "up"])

# print("[+] MAC address for "+interface+" has been changed successfully")
exit("[+] MAC address for "+interface+" has been changed to "+new_mac_address)
