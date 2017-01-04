## Excercise 0  myclient_ex0 ###
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

def splitNum(num): #USE for COOKIE 
	higherB = num >> 16
	lowerB = num - (higherB << 16)
	return higherB, lowerB

datagram = array.array('l')
def makeDatagram(value):
    #value = bin(value)[2:].zfill(16)
    datagram.append(value)
    return datagram


serverPort = 35604                              #server listens for connectionso on ports 35601, 35602, 35603
host = '128.83.144.56'                          #server run on paris.cs.utexas.edu (IP address 12\8.83.144.56)
attempt = 1                                     #variables keeping track of attempts
addr = (host, serverPort)
carry_over = 1

#(i)
clientSocket = socket(AF_INET, SOCK_DGRAM)      #create a socket
#clientSocket.connect((host,serverPort))         #client opens a connection to the server's socket

#(ii)
#create message structure
#creating the first Field, the Header, 16bit + 16bit
classNumber = '0 00001 0110 0100'                                   	 #the value 356 in binary
messageType = '0'                                                  #most sign bit. excercise 0
request = '0'                                                   	 #next-most sign bit. set: 0-request 1-response
first16_Field1_int_a = 356 #0000000101100100
first16_Field1_binary = bin(356)[2:].zfill(16)
# print 'Datagram A:', first16_Field1_binary

labNumber = '00000001'                                             #0x01 in hex
versionNumb = '00000111'                                           #0x07, version of the lab
second16_Field1_int_b = 263 #0000000100000111
second16_Field1_binary = bin(263)[2:].zfill(16)
# print 'Datagram B:', second16_Field1_binary

makeDatagram(356)
makeDatagram(263)


#creating the second Field, the Client Cookie, 32 bit
#turn into int
cookie = 1685167145 #'0110 0100 0111 0001 1001 1100 0010 1001' 
bin_cookie = bin(1685167145)[2:].zfill(32)
first16_Field2_int_c = 25713
first16_Field2_binary = bin(25713)[2:].zfill(16)
second16_Field2_int_d = 39977
second16_Field2_binary = bin(39977)[2:].zfill(16)
cookie_split = splitNum(cookie)
# print 'Datagram C:', first16_Field2_binary
# print 'Datagram D:', second16_Field2_binary

makeDatagram(25713)
makeDatagram(39977)


#(iii)
#creating the third Field, the Request Data, SSN, 32 bit
SSN_3Field_int_e = int(input("Enter Social Security Number: "))
SSN_split,SSN_split2 = splitNum(SSN_3Field_int_e)
SSN_3Field_int_e = bin(SSN_split)[2:].zfill(16)
SSN_3Field_int_f = bin(SSN_split2)[2:].zfill(16)
makeDatagram(SSN_split)
makeDatagram(SSN_split2)

# SSN = bin(412324869)[2:].zfill(32)  #corresponding PO 4292
# SSN1,SSN2 = splitNum(412324869)
# SSN_3Field_int_e = bin(SSN1)[2:].zfill(16)
# SSN_3Field_int_f = bin(SSN2)[2:].zfill(16)
# print 'Datagram E:', SSN_3Field_int_e
# # print 'Datagram F:', SSN_3Field_int_f

# makeDatagram(SSN1)
# makeDatagram(SSN2)

#(iv)
#creating the fourth Field, CheckSum and Result fields,  16bit + 16bit
checksum = 0
checksum_binary = bin(checksum)[2:].zfill(16)
# print 'Datagram G:', checksum_binary

# print '-----------------'
# for i in range(0,6):
#     print datagram[i]
# print '-----------------'

summation =  bin(int(bin(356)[2:].zfill(16),2) + int(bin(263)[2:].zfill(16),2))[2:].zfill(16)
length = len(summation)
if(length > 17):
    summation= summation + 1

summation = bin(int(summation,2) + (int(bin(25713)[2:].zfill(16),2)))[2:].zfill(16)
length = len(summation)
if(length > 17):
    summation= summation + 1

summation = bin(int(summation,2) + (int(bin(39977)[2:].zfill(16),2)))[2:].zfill(16)
length = len(summation)
if(length > 17):
    summation= summation + 1

summation = bin(int(summation,2) + (int(bin(6291)[2:].zfill(16),2)))[2:].zfill(16)
length = len(summation)
if(length > 17):
    summation= summation + 1

summation = bin(int(summation,2) + (int(bin(37893)[2:].zfill(16),2)))[2:].zfill(16)
length = len(summation)
if(length > 17):
    summation= summation + 1

#print 'Summation', summation       11010111110011101
#print 'Complement:', ~Summatio     00101000001100010
checksum = 20578
checksum_binary = bin(checksum)[2:].zfill(16)
# print 'Datagram G:', checksum_binary
makeDatagram(checksum)

#viewing the msg a squence of eight 16-bit integers
#add them using ones complement arithmetic
# length = 16 
# intialSUM = 0; 
# for i in range(0,6):

#     if range(0):
#         print 'only once'
#         summation = datagram[i]
#         checksum = datagram[i]
#         length = len(bin(checksum)[2:].zfill(16))
#         i = i + 1

#     print 'checkSum', checksum    
#     print 'adding:', datagram[i]
#     print 'test', 

#     if length < 17:
#         print 'inside'
#         checksum = datagram[i] + summation
#         length = len(bin(checksum)[2:].zfill(16))

#     else:
#         print ' else'
#         checksum = checksum + 1
#         length = len(bin(checksum)[2:].zfill(16))

#     print 'checksum', checksum
   

result_binary = bin(0)[2:].zfill(16)
result = 0
# print 'Datagram H:', result_binary

makeDatagram(result)

s = pack('!HHHHHHHH', *datagram)

tries = 0
message = s
#(v) start a timer (to detect lost messages) using timeout()
clientSocket.settimeout(5)
clientSocket.connect((host,serverPort))

while tries < 5:
    try:
        data, address = clientSocket.recvfrom(1024) 
        #(vii) receive the response message using recvfrom()
        print 'Message Received || PO Box Number: 4292'
        #(ix) when the response message receied, check for proper attributes

#(vi) send the request message to server (identified by IP address and port)
#(viii) if the time expries, send the request message again, up to some max number of retransmissions
    except timeout:
        clientSocket.sendto(message,(host,serverPort))
        clientSocket.settimeout(5)
        tries += 1
        continue

    else:
        break
