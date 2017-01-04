## Excercise 0  myserver.py ###
#Patrizio Chiquini
#UTEID: pc22566 UTCS: chiquini

from socket import *
from struct import *
import sys
import time
import random
import array
#function to print binary number for the SSN input
# def binary(n):
#   return [int(i) for i in bin(x)[2:]]
#   #return tobin(x/2) + [x%2] if x > 1 else [x]

#128.83.130.18

def packPkt(ar): #does it in 16 bit chunks
	pkt = ''
	for i in range(0, len(ar)):
	   pkt = pkt + struct.pack('!H', ar[i])
	return pkt

serverPort = 35604                              #server listens for connectionso on ports 35601, 35602, 35603
secondPort = 35602
host = '128.83.144.56'                          #server run on paris.cs.utexas.edu (IP address 12\8.83.144.56)
attempt = 1                                     #variables keeping track of attempts
addr = (host, serverPort)
carry_over = 1

#(2) Create a socket of type SOCK_DGRAM and family AF_INET
clientSocket = socket(AF_INET, SOCK_DGRAM)      #create a socket
#clientSocket.connect((host,serverPort))        #client opens a connection to the server's socket

#(3) Bind the socket to some port using bind()
currentHost = gethostbyname(gethostname())      #IP address of the current machine in use
clientSocket.bind((currentHost,secondPort))     #bind the socket to an available port 
#clientSocket = ((UDP_IP, SUT_PORT))

#(4) Loop forever, doing the following 

while True:
    data, address = clientSocket.recvfrom(1024) #receive a datagram
    # if(format and checksum incorrect):
        #     return appropriate error code
        # else if:
        #     look up in the database the PO Box Number for the SSN from request
        #     if SSN present:
        #         fill in the result field of the response
        #         recopmute the checksum
        #         send the response datagram back whence it came using sendto