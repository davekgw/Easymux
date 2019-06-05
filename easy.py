## easy.py - Easymux v3.5
# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
from esmcore import *

def main():
	banner()
	print "   [01] Tool For Get_Information(2)"
        print "   [02] Tool Facebook(3)"
        print "   [03] Tool Web(2)\n"
	print "   [00] Exit the Easymux\n"
	easymux = raw_input("Easymux > ")
	
	if easymux == "01" or easymux == "1":
		print "    [01] OSIF"
                print "    [02] GPS_Tracking"
		print "    [00] Back to main menu\n"
		infogathering = raw_input("Info > ")
		
		if infogathering == "01" or infogathering == "1":
			osif()
		elif infogathering == "02" or infogathering == "2":
			gps()
		elif infogathering == "00" or infogathering == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

        elif easymux == "02" or easymux == "2":
                print "    [01] SpamChat"
                print "    [02] UnFriendFB"
                print "    [03] MultiBruteForce\n"
		print "    [00] Back to main menu\n"
		toolfb = raw_input("ToolFB > ")

                if toolfb == "01" or toolfb == "1":
			spamchat()
                elif toolfb == "02" or toolfb == "2":
			unfriend()
                elif toolfb == "03" or toolfb == "3":
                        force()
                elif toolfb == "00" or toolfb == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif easymux == "03" or easymux == "3":
                print "    [01] Web_Deface"
                print "    [02] DownWeb\n"
                print "    [00] Back to main menu\n"
                web = raw_input("ToolWeb > ")
                
                if web == "01" or web == "1":
			webdef()
                elif web == "02" or web == "2":
                        downweb()
                elif web == "00" or web == "0":
			restart_program()
                else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
        elif easymux == "00" or easymux == "0":		
                sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
