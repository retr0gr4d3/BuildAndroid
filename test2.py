import os
import sys, traceback

def main():
	try:
		print('''
 \033[1;36m
                           $$\                               $$\
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
			''')
		def start1():
			while True:
				print ('''
1) Install the tools needed to build
2) Sync ROM
3) Clone required repos
4) Build ROM for Blueline
5) Build ROM for Crosshatch

6) Remove ROM directory
7) Remove cloned repos
8) Make Clean

9) Configure Git details

99) Help
					''')
				option0 = input("\033[1;36mBuildAndroid> \033[1;m")

				if option0 == "1":
					print ("Installing required tools...")
					cmd1 = os.system("sudo apt install -y bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev libncurses5 git repo openjdk-8-jdk adb fastboot")
					print ("Tools installed!")
				elif option0 == "2":
					print ('''
Syncing the ROM can take hours to complete, depending on your WiFi
speed. Please remain patient while this completes.
						''')
					print ("Creating ROM directory...")
					cmd1 = os.system("cd")
					cmd2 = os.system("mkdir ~/bliss")
					print ("Directory created!")
					print ("Initializing repo in new directory...")
					cmd3 = os.system("cd $HOME/bliss")
					cmd4 = os.system("repo init -u https://github.com/BlissRoms/platform_manifest.git -b q")
					cmd5 = os.system("repo sync --current-branch --force-sync --no-clone-bundle --no-tags --optimized-fetch --prune")
					print ("Sync complete!")
				elif option0 == "3":
					print ("oi")
				elif option0 == "4":
					print ("oi")
				elif option0 == "5":
					print ("oi")
				elif option0 == "6":
					print ("oi")
				elif option0 == "7":
					print ("oi")
				elif option0 == "8":
					print ("oi")
				elif option0 == "9":
					print ("oi")
				elif option0 == "99":
					print ("oi")
				else:
					print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

		start1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()