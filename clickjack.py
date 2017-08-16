import urllib.request
import urllib.parse
import requests
import sys
import time
import os
import string

site =''
while not site :
   print('Target Site:')
   site=input()
   break
r =urllib.request.urlopen("http://"+site)
x= r.getheader('X-Frame-Options')
if (x== "DENY" or x == "SAMEORIGIN"):
    print("Not Vulnerable to ClickJacking")
else:
    print("Bingo! You caught Clickjacking, now exploit it ;) ")

banner = """

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



