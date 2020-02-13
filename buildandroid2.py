#!/usr/bin/python

import os
import sys, traceback


if os.getuid() != 0:
	print "Sorry. This script reqires root privledges. Please elevate and try again. :("
	sys.exit()


def main():
	try:
		print('''

 \033[1;36m                          $$\                               $$\
                           $$ |                    $$\       $$ |
                           $$ |                    \__|      $$ |
  $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$$\  $$$$$$\  $$\  $$$$$$$ |
  \____$$\ $$  __$$\ $$  __$$ |$$  _____|$$  __$$\ $$ |$$  __$$ |
  $$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |
 $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |
 \$$$$$$$ |$$ |  $$ | $$$$$$  |$$ |      \$$$$$$  |$$ | $$$$$$  |
  \_______|\__|  \__| \______/ \__|       \______/ \__| \______/  \033[1;m

        +------------------------------------------------+
        | Android Building made  noob-friendly by a noob |
        +------------------------------------------------+

 \033[1;32m+ -- -- +=[ Using Katoolin V2.0 as a template
 \033[1;32m+ -- -- +=[ Author: Retr0gr4d3 - git.retr0.gr4d3.uk\033[1;m
 \033[1;32m+ -- -- +=[ Made with Python, love and good intentions

 \033[1;91m[WARNING] This software will made modifications to your system.

           This will install new tools, in order to build Android OS.\033[1;m
		''')
		def start1():
			while True:
				print ('''
1) Add repos, update, Install, view sources
2) View Categories
3) Classicmenu shit
4) kali menu shit
5) Help

			''')

				opcion0 = raw_input("\033[1;36mBuildAndroid > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) Add required repositories
2) Update repositories
3) Install apps
4) View the contents of sources.list file

					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# All ubuntu repositories | Added by Retr0gr4d3\ndeb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						

				if opcion0 == "3":
					print (''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

''')
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				elif opcion0 == "5":
					print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

		''')


				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) first on category			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

			 ''')
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt install *")	
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ First on category\033[1;m

1) first on category
2) first on category

0) Install all first on category
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install first on category")
							elif opcion2 == "2":
								cmd = os.system("apt-get install first on category")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y first on category")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

1) BBQSQL
2) BED

0) Install all Vulnerability Analysis tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install bbqsql")
							elif opcion2 == "2":
								cmd = os.system("apt-get install bed")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y ")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "3":
							print ('''
\033[1;36m=+[ Wireless Attacks\033[1;m

1) Aircrack-ng
2) Asleap

0) Install all Wireless Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install aircrack-ng")
							elif opcion2 == "2":
								cmd = os.system("apt-get install asleap")
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4":
							print ('''
\033[1;36m=+[ Web Applications\033[1;m

1) apache-users
2) Arachni

0) Install all Web Applications tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apache-users")
							elif opcion2 == "2":
								cmd = os.system("apt-get install arachni")										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt install -y")												
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "5":
							print ('''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

1) Burp Suite
2) DNSChef

0) Install all Sniffing & Spoofing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install burpsuite")
							elif opcion2 == "2":
								cmd = os.system("apt-get install dnschef")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "6":
							print ('''
\033[1;36m=+[ Maintaining Access\033[1;m

1) CryptCat
2) Cymothoa

0) Install all Maintaining Access tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install cryptcat")
							elif opcion2 == "2":
								cmd = os.system("apt-get install cymothoa")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y ")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "7":
							print ('''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt

0) Install all Reporting Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install casefile")
							elif opcion2 == "2":
								cmd = os.system("apt-get install cutycapt")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "8":
							print ('''
\033[1;36m=+[ Exploitation Tools\033[1;m

1) Armitage
2) Backdoor Factory

0) Install all Exploitation Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install armitage")
							elif opcion2 == "2":
								cmd = os.system("apt-get install backdoor-factory")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y ")  						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "9":
							print ('''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk
 2) Bulk Extractor

0) Install all Forensics Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install binwalk")
							elif opcion2 == "2":
								cmd = os.system("apt-get install bulk-extractor")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y ")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "10":
							print ('''
\033[1;36m=+[ Stress Testing\033[1;m

1) DHCPig
2) FunkLoad		

0) Install all Stress Testing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install dhcpig")
							elif opcion2 == "2":
								cmd = os.system("apt-get install funkload")  				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y ")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "11":
							print ('''
\033[1;36m=+[ Password Attacks\033[1;m

1) acccheck
2) Burp Suite

0) Install all Password Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install acccheck")
							elif opcion2 == "2":
								cmd = os.system("apt-get install burpsuite")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "12" :
							print ('''
\033[1;36m=+[ Reverse Engineering\033[1;m

1) apktool
2) dex2jar

0) Install all Reverse Engineering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install apktool")
							elif opcion2 == "2":
								cmd = os.system("apt-get install dex2jar")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "13" :
							print ('''
\033[1;36m=+[ Hardware Hacking\033[1;m

1) android-sdk
2) apktool

0) Install all Hardware Hacking tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt-get install android-sdk")
							elif opcion2 == "2":
								cmd = os.system("apt-get install apktool")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "14" :
							print ('''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
				''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install -y")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt-get install -y")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
