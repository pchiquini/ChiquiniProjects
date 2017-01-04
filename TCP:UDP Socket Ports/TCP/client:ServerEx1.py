client/ServerEx1.py
### Excercise 1 Client/Server ###
#Patrizio Chiquini
#UTEID: pc22566 UTCS: chiquini

#!/usr/bin/env python

from socket import *
from struct import *
import sys #in order to receive the input from cmd line
import time
import random

serverPort = 35601                              #server listens for connectionso on ports 35601, 35602, 35603
secondPort = 35602
host = '128.83.144.56'                          #server run on paris.cs.utexas.edu (IP address 128.83.144.56)

psock = socket(AF_INET, SOCK_STREAM)            #creating the server'socket

currentHost = gethostbyname(gethostname())      #IP address of the current machine in use

psock.bind((currentHost,secondPort))            #bind the socket to an available port

Bounded_psock = psock.getsockname( )
print '\nSocket Binding Completed:'
print 'Connected to the Address: ' + str(Bounded_psock[0]) + ' Port: ' + str(Bounded_psock[1]) + '\n'

psock.listen(1)

clientSocket = socket(AF_INET, SOCK_STREAM)     #creating the client'socket
clientSocket.connect((host,serverPort))         #client opens a connection to the server'\s socket

#creating the CLIENT request string SAME AS EX0
usernum = random.randint(0,9000)
requestType = 'ex1 '
clientEndPoint = clientSocket.getsockname( )
connectionSpecifier = host + '-' + str(serverPort) + ' ' + str(clientEndPoint[0]) + '-' +\
 str(secondPort) + ' '
username = ' P.Chiquini \n'
send_sentence = requestType + connectionSpecifier + str(usernum) + username

clientSocket.send(send_sentence)                #first openned connection to the server and send the request
                                                #server sends back a confirmation on the original connection
confirmationString = clientSocket.recv(1024)    #first line contains an identification and the date and time
confirmationString2 = clientSocket.recv(1024)   #second line will contain the string 'OK', and ID information
print confirmationString
print confirmationString2

if (confirmationString2.split()[0] == 'OK'):    #if the server confirmation is OK, clientsends an ack string as follow
    serverRandomNum = int(confirmationString2.split()[3])
    newsock, addr = psock.accept()              #socket unitiaed by server. Serve as our second connection
    recv_sentence = newsock.recv(1024)          #read bytes from connection socket
    print 'Accepting Second Connection: \n' + recv_sentence

    if(recv_sentence.split()[0] == None):       #None. indicates that the other end of the second connection has stopped sending
        print 'None. Shutting Down'
        newsock.close()
                                                								  #Therefore, we can close it
    else:
        new_serverRandomNum = int(recv_sentence.split()[4])  					  #get the new random numberfrom server
        print 'Client Resposne: \nCS 356 server sent ' + str(new_serverRandomNum) #if random number received, print this line
        newString = str(serverRandomNum+1) + ' ' + str(new_serverRandomNum+1) + '\n'
        newsock.send(newString)                               					  #send() the string
        recv_sentence2 = clientSocket.recv(1024)               					  #receive date on the original connection
        newsock.close()
        clientSocket.close()

else:
    print 'No OK received. Closing Connection'
    clientSocket.close()

print '\nServer Second Confirmation: \n' + recv_sentence2     					#print out the result
psock.close()                                   								#close the original connection

