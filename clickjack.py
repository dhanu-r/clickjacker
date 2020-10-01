import urllib.request
import urllib.parse
import requests
import sys
import time
import os
import string

banner="""

#   $$$$$$\  $$\ $$\           $$\          $$$$$\                     $$\                           	#
#  $$  __$$\ $$ |\__|          $$ |         \__$$ |                    $$ |                          	#	
#  $$ /  \__|$$ |$$\  $$$$$$$\ $$ |  $$\       $$ | $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  	#
#  $$ |      $$ |$$ |$$  _____|$$ | $$  |      $$ | \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 	#
#  $$ |      $$ |$$ |$$ /      $$$$$$  / $$\   $$ | $$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|	#	
#  $$ |  $$\ $$ |$$ |$$ |      $$  _$$<  $$ |  $$ |$$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |      	#
#  \$$$$$$  |$$ |$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      	#
#   \______/ \__|\__| \_______|\__|  \__| \______/  \_______| \_______|\__|  \__| \_______|\__|      	#	
#                                                                                                    	#
#                                                                                                    	#	
#                                                                                                    	#


Coded By HAXORMAD (AbaRTan DhAKal) ;) 
Your Very Own ClickJAcking Finder
"""
print(banner)

site =''
while not site :
   print('Target Site:')
   site=input()
   break
r =urllib.request.urlopen("http://"+site)      #Online Scanner: https://clickjacker.io/
x= r.getheader('X-Frame-Options')    
if (x== "ALLOW" or x == "allow"):
    print("Bingo! You caught Clickjacking, now exploit it ;) ")
else:
    print("Not Vulnerable to ClickJacking")

