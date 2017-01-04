### Excercise 0  CLIENT ###
#Patrizio Chiquini
#UTEID: pc22566 UTCS: chiquini

from socket import *
from struct import *
import sys
import time
import random

serverPort = 35601                              #server listens for connectionso on ports 35601, 35602, 35603
host = '128.83.144.56'                 			#server run on paris.cs.utexas.edu (IP address 12\8.83.144.56)

clientSocket = socket(AF_INET, SOCK_STREAM)     #creating the client'socket
clientSocket.connect((host,serverPort))         #client opens a connection to the server's socket

#creating the request string that will be sent from the client
usernum = random.randint(0,9000)
requestType = 'ex0 '
clientEndPoint = clientSocket.getsockname( )
connectionSpecifier = host + '-' + str(serverPort) + ' ' + str(clientEndPoint[0]) + '-' +\
 str(clientEndPoint[1]) + ' '
username = ' P.Chiquini \n'
send_sentence = requestType + connectionSpecifier + str(usernum) + username

#once the client has been connected, it immediately sends a request string
clientSocket.send(send_sentence)
#print '*** Waiting For The Server***\n'

#server sends back a confirmation in the form of one or more lines
recv_sentence = clientSocket.recv(1024)                 #first line contains an identification and the date and time
recv_sentence2 = clientSocket.recv(1024)                #second line will contain the string 'OK', and ID information
print recv_sentence
print recv_sentence2
servernum1 = int(recv_sentence2.split()[3])

if (recv_sentence2.split()[0] == 'OK'):                 #if the server confirmation is OK, client sends an ack string as follow
    client_ack = requestType + str(usernum+1) + ' ' + str(servernum1+1) + '\n'
    clientSocket.send(client_ack)
    server_ack = clientSocket.recv(1024)                #upon client ack, the server sends back an ack
    print server_ack

clientSocket.close()