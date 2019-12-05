## easy.py - Easymux v3.5
# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
from esmcore import *

def main():
	banner()
	print "   [01] Tool For Get_Information"
        print "   [02] Tool Facebook"
        print "   [03] Tool Web\n"
	print "   [00] Exit the Easymux\n"
	easymux = raw_input("Easymux > ")
	
	if easymux == "01" or easymux == "1":
		print "    [01] OSIF"
                print "    [02] GPS_Tracking"
		print "    [00] Back to main menu\n"
		infogathering = raw_input("ToolInfo > ")
		
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
		print "    [01] OSIF"
                print "    [02] SpamChat"
                print "    [03] UnFriendFB"
                print "    [04] MultiBruteForce"
                print "    [05] YahooCloning"
		print "    [06] FbBrute"
		print "    [07] FB Profile Guard"
		print "    [08] Dark Fb\n"
		print "    [00] Back to main menu\n"
		toolfb = raw_input("ToolFB > ")
                if toolfb == "01" or toolfb == "1":
			osif()
                elif toolfb == "02" or toolfb == "2":
			spamchat()
                elif toolfb == "03" or toolfb == "3":
			unfriend()
                elif toolfb == "04" or toolfb == "4":
                        force()
                elif toolfb == "05" or toolfb == "5":
                        yclon()
		elif toolfb == "06" or toolfb == "6":
		        brute()
                elif toolfb == "07" or toolfb == "7":
	                guard()
                elif toolfb == "08" or toolfb == "8":
	                dark()
                elif toolfb == "00" or toolfb == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()

	elif easymux == "03" or easymux == "3":
                print "    [01] Web_Deface"
                print "    [02] DownWeb"
                print "    [03] YahooCloning"
	        print "    [04] Termux Theme\n"
                print "    [00] Back to main menu\n"
                web = raw_input("ToolWeb > ")
                
                if web == "01" or web == "1":
			webdef()
                elif web == "02" or web == "2":
                        downweb()
                elif web == "03" or web == "3":
                        yclon()
                elif web == "04" or web == "4":
		        theme()
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
