import re
import subprocess
import optparse



parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface_name", help="-h")
parser.add_option("-m", "--address", dest="new_mac_address", help="-h")
options, arguments = parser.parse_args()

if not options.interface_name:
    parser.error("Usage: python3 mac_changer.py -i <Your Interface Here> -m <Choice New Mac Address For Your Interface")
    exit()

if not options.new_mac_address:
    parser.error("Usage: python3 mac_changer.py -i <Your Interface Here> -m <Choice New Mac Address For Your Interface")
    exit()

nic_check = subprocess.check_output("ifconfig", shell=True).decode("utf-8")

if str(options.interface_name) in str(nic_check):
    
    
    ifconfig = subprocess.check_output(f"ifconfig {options.interface_name}", shell=True).decode("utf-8")
    old_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)[0]

    

    if old_mac != options.new_mac_address and len(options.new_mac_address)==17:

        subprocess.call(f"ifconfig {options.interface_name} down", shell=True)
        subprocess.call(f"ifconfig {options.interface_name} hw ether {options.new_mac_address}", shell=True)
        subprocess.call(f"ifconfig {options.interface_name} up", shell=True)

        print(f"[+] Your Mac Address has been changed from {old_mac} to {options.new_mac_address}")
        print("\n\nCreated By HowAreYouNow!")

    else:
        print("[-] Use other Mac Address OR Use a correct Mac Address format")

else:
    print(f"[-] {options.interface_name}: Device not found")
