## lzmcore.py - useful module of Lazymux
# -*- coding: utf-8 -*-
import os
import sys
import time

lazymux_banner = """
.____ 
: .__'                                        
: :__                                           
: .__' .--.  .---. .-..-.,-.,-.,-..-..-..-.,-.
: :__ ' .; ; `-'_.': :; :: ,. ,. :: :; :`.  .'
:___.'`.__,_;`.___;`._. ;:_;:_;:_;`.__.':_,._;
                    .-. :                     
                    `._.'  
By : Dave Koagow                   
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazymux
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("lzmx > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
	print lazymux_banner

def spamchat():
	print '\n###### Installing SpamChatting'
	os.system('git clone https://github.com/davekgw/chatting')
	os.system('mv chatting ~')
	print '###### Done'
	backtomenu_option()

def osif():
	print '\n###### Installing OSIF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/ciku370/OSIF')
	os.system('mv OSIF ~')
	print '###### Done'
	backtomenu_option()

def gps():
	print '\n###### Installing GPS_Tracking'
	os.system('apt update && apt upgrade')
	os.system('pkg install python2 git wget')
        os.system('pip2 install --upgrade pip')
        os.system('pip2 install mechanize')
        os.system('pip2 install request')
	os.system('git clone https://github.com/davekgw/gps_tracking')
	os.system('mv chatting ~')
	print '###### Done'
	backtomenu_option()
