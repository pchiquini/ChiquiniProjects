### Excercise 0  Implementing a Client ###
#Patrizio Chiquini
#UTEID: pc22566 UTCS: chiquini

from socket import *
from struct import *
import sys
import time
import random

serverPort = 35604                              #server listens for connectionso on ports 35601, 35602, 35603
host = '128.83.144.56'                 			#server run on paris.cs.utexas.edu (IP address 12\8.83.144.56)

#(i)
clientSocket = socket(AF_INET, SOCK_DGRAM)      				#create a socket
clientSocket.connect((host,serverPort))         #client opens a connection to the server's socket

#(ii)
#create message structure
#creating the first Field, the Header, 16bit + 16bit
classNumber = '00 0001 0110 0100 '									#the value 356 in binary
messageType = '0'        											#most sign bit. excercise 0
request = '0' 													#next-most sign bit. set: 0-request 1-response
labNumber = '0000 0001 '											#0x01 in hex
versionNumb = '0000 0111'											#0x07, version of the lab
header_1Field =  messageType + request + classNumber + labNumber + versionNumb

#creating the second Field, the Client Cookie, 32 bit
cookie = '0000 0000 0000 0000 0000 0000 0000 0001' 	#arbitary value cookie = random.randint(0,9000)
clientCookie_2Field = cookie

#(iii)
#creating the third Field, the Request Data, SSN, 32 bit
SSN = input("Enter Social Security Number: ")
SSN = int(SSN)
requestData_3Field = SSN

#(iv)
#creating the fourth Field, CheckSum and Result fields,  16bit + 16bit
Checksum = 0
#viewing the msg a squence of eight 16-bit integers
#add them using ones complement arithmetic
#and take ones complement of the sum
#write the result in Checksum field of the message (overwriting the zero value)
result #unused in request. 
	#0000 0000 = success -> the low-order 15 bits contain the PostOfficeBox number, encoded as integer
	#0000 0001 = error -> the following four integer values of the low-order 15 bits encode 4 types of errors
		#ChecksumError
		#SyntaxError
		#Unknown SSN
		#Server Error
check_4Field = Checksum + result


#(v)
clientSocket.settimeout(10)					#start a timer to detect lost messages
clientSocket.connect((host,serverPort))
clientSocket.settimeout(None)				#set the socket into blocking mode


#(vi)
#send the request message to server (using its IP address and port)
#do not forget to convert each multi-byte field in the message to network byte order
messageStructure = header_1Field + clientCookie_2Field + requestData_3Field + check_4Field
clientSocket.sendto(messageStructure,(host, serverPort))

#(vii)
#receive the response message 
responseMsg = clientSocket.recvfrom(1024)
#responseMsg.split()[32]

#(viii)
#if timer expires, send the request message again, only attempt this 5 times

#(ix)
#check response msg received, recomputer checksum,
if( 'responseMsg is good' ):
	print 'P.O. Box Number: '
else
	print 'Error'








