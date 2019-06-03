## lazymux.py - Lazymux v3.0
# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
from lzmcore import *

def main():
	banner()
	print "   [1] Information Gathering\n"
	print "   [2] Exit the Lazymux\n"
	lazymux = raw_input("lzmx > ")
	
	if lazymux == "01" or lazymux == "1":
		print "    [01] OSIF"
                print "    [02] GPS_Tracking"
                print "    [03] SpamChat\n"
		print "    [00] Back to main menu\n"
		infogathering = raw_input("lzmx > ")
		
		if infogathering == "01" or infogathering == "1":
			osif()
		elif infogathering == "02" or infogathering == "2":
			gps()
		elif infogathering == "03" or infogathering == "3":
			spamchat()
		elif infogathering == "00" or infogathering == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif lazymux == "02" or lazymux == "2":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
