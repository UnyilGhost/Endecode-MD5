import hashlib
import os
import time
import urllib
import urllib2
import re

B = '\033[1;36m'
R = '\033[1;31m'
W = '\033[1;0m'
H = '\033[1;33m'
K = '\033[1;34m'

os.system("clear")

index = """\033[1;31m
_    _             _ _  _____ _               _   
| |  | |           (_) |/ ____| |             | |  
| |  | |_ __  _   _ _| | |  __| |__   ___  ___| |_ 
| |  | | '_ \| | | | | | | |_ | '_ \ / _ \/ __| __|
| |__| | | | | |_| | | | |__| | | | | (_) \__ \ |_ 
 \____/|_| |_|\__, |_|_|\_____|_| |_|\___/|___/\__|
               __/ |                               
              |___/                                
    https://github.com/UnyilGhost
            UnyilGhost
[#] 1. Encrpyt Md5 [#] 
"""

print(index)


def Menu():
	os.system("clear")
	print(index)
	print("""\033[1;36m
	 Md5 Encrypt
""")

def main():
		x = raw_input("[?]>>>")
		if x == "--Menu":
			time.sleep(2)
			Menu()
			main()
		
	
		elif x == "1":
			os.system("clear")
			print(index)
			b = raw_input("\033[1;34m[Md5 Encrpyt]>>")
			md5 = hashlib.md5(b.encode())
			print "Code You>>>",md5.hexdigest()
			print ""
			main()
			
		else:
			print ""
			print "\033[1;32mCommand >> --Pilih Nomer Yang Ada Di Menu?"
			print ""
			print "\033[1;33mNo Command >>",x
			print ""
			main()
if __name__ == "__main__":
	main()
