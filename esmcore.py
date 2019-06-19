## esmcore.py - useful module of Easymux
# -*- coding: utf-8 -*-
import os
import sys
import time

easymux_banner = """
\033[1;36m.____ 
: .__'                                        
: :__                                           
: .__' .--.  .---. .-..-.,-.,-.,-..-..-..-.,-.
: :__ ' .; ; `-'_.': :; :: ,. ,. :: :; :`.  .'
:___.'`.__,_;`.___;`._. ;:_;:_;:_;`.__.':_,._;
                    .-. :                     
                    `._.'  
\033[1;33mAll Scripts on this tool 
\033[1;37mMakeBy : \033[1;31mDave Koagow  

\033[1;31mTool ini tidak di perjual belikan!\033[0m
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Easymux
"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("esmx > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong Input"
		time.sleep(2)
		restart_program()

def banner():
	print easymux_banner

def spamchat():
	print '\n###### Installing SpamChatting'
	os.system('apt update && apt upgrade')
	os.system('pkg install python2 git')
	os.system('pip2 install requests')
	os.system('pip2 install mechanize')
	os.system('git clone https://github.com/davekgw/chatting')
	os.system('mv chatting ~')
	print '###### Done'
	backtomenu_option()

def osif():
	print '\n###### Installing OSIF'
	os.system('apt update && apt upgrade')
        os.system('clear')
	os.system('apt install git python2')
        os.system('clear')
	os.system('pip2 install requests')
        os.system('clear')
	os.system('git clone https://github.com/davekgw/osiff')
        os.system('clear')
	os.system('mv osiff OSIF')
        os.system('clear')
	print '###### Done'
	backtomenu_option()

def gps():
	print '\n###### Installing GPS_Tracking'
	os.system('apt update && apt upgrade')
	os.system('pkg install python2 git php wget')
        os.system('pip2 install --upgrade pip')
        os.system('pip2 install mechanize')
        os.system('pip2 install request')
	os.system('git clone https://github.com/davekgw/gps_tracking')
	os.system('mv GpsTracking ~')
	print '###### Done'
	backtomenu_option()

def unfriend():
	print '\n###### Installing UnFriendFB'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests')
        os.system('pip2 install mechanize')
	os.system('git clone https://github.com/davekgw/UnFriendFB')
	os.system('mv UnFriendFB ~')
	print '###### Done'
	backtomenu_option()

def webdef():
	print '\n###### Installing Web_Deface'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests')
	os.system('pip2 install mechanize')
	os.system('pip2 install --upgrade pip')
	os.system('git clone https://github.com/davekgw/Deface-Web')
	os.system('mv DefaceWeb ~')
	print '###### Done'
	backtomenu_option()

def downweb():
	print '\n###### Installing DownWebsite'
	os.system('apt update && apt upgrade')
	os.system('pkg install git python2')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/davekgw/DownWeb')
	os.system('mv DownWeb ~')
	print '###### Done'
	backtomenu_option()

def force():
        print '\n###### Installing MBForce'
        os.system('apt update && apt upgrade')
        os.system('pkg install python2 git wget')
        os.system('pip2 install --upgrade pip')
        os.system('pip2 install mechanize requests request')
        os.system('git clone https://github.com/davekgw/Force')
        os.system('mv Force')
        print '###### Done'
        backtomenu_option()
	
def yclon():
        print '\n###### Installing YahooCloning'
        os.system('pkg update && pkg upgrade')
        os.system('pkg install python2 git')
        os.system('pip2 install mechanize requests')
        os.system('git clone https://github.com/davekgw/YahooClone')
        os.system('mv Clonning')
        print '###### Done'
        backtomenu_option()

def brute():
        print '\n###### Installing FbBrute'
        os.system('apt update && apt upgrade')
        os.system('clear')
        os.system('pkg install python2 git')
        os.system('clear')
        os.system('git clone https://github.com/davekgw/FbBrute')
        os.system('clear')
        os.system('mv FbBrute Brute')
        print '###### Done'
        backtomenu_option()
