from socket import *
import array 
import random 
import sys 
import re
import struct
import datetime

def splitNum(num, shift): 
    higher = num >> shift 
    lower = num - (higher << shift) 
    return higher, lower

def computeChecksum(array):
    checksum = 0
    for i in range(0, len(array)):
        checksum += array[i]
        checksum = (checksum & 0xffff) + (checksum >> 16)
    return checksum

def packPkt(ar): 
    pkt = '' 
    for i in range(0, len(ar)): 
        pkt = pkt + struct.pack('!H', ar[i])
    return pkt 

def combineNum(higherB, lowerB):
    num = (0 | higherB) << 16
    num = num | lowerB
    return num

def report(ar):
    print '\tType: ', (ar[0] >> 15) & 0x1
    print '\tFlag: ', ((ar[0] << 1) >> 15) & 0x1
    print '\t\t', ((ar[0] << 2) >> 2) & 0x3fff
    print '\tLab: ', splitNum(ar[1], 8)[0]
    print '\tVersion: ',  splitNum(ar[1], 8)[1]
    print '\tCookie: ', combineNum(ar[2], ar[3])
    print '\tSSN: ', combineNum(ar[4], ar[5])
    print '\tChecksum: ', ar[6]
    print '\tOutcome: ', (ar[7] >> 15) & 0x1
    print '\tResult: ', ((ar[7] << 1) >> 1) & 0x7fff

# Client Opeation (iii) - Get ssn
userIn = raw_input('Please enter your nine digit social security number: ')

# Check for a nine digit number
if re.match('^\d{9}$', userIn):
    ssn = int(userIn)
else:
    sys.exit("Invalid input")
# Client Operation (ii) - Fill in message structure
# 0000 0001 0110 0100 0000 0001 0000 0111 <==> 0x01640107
request = array.array('H', [0x0164, 0x0107])
# (2 ^ 32) - 1 <==> 4294967295
cookie = random.randint(0, 4294967295)
splitCookie = splitNum(cookie, 16)
request.append(splitCookie[0])
request.append(splitCookie[1])
splitSSN = splitNum(ssn, 16)
request.append(splitSSN[0])
request.append(splitSSN[1])
# Client Operaton (iv) - Compute checksum
checksum = ~computeChecksum(request) & 0xffff
request.append(checksum)
request.append(0)
reqPckt = packPkt(request)

serverName = '128.83.144.56'
serverPort = 35605
# Client Operation (i) - Create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Client Operation (v) - Start timer
clientSocket.settimeout(5)
timeCount = 0

# Client Operation (vi) to (viii) - Send request and receive response 
while timeCount < 6:
    clientSocket.sendto(reqPckt, (serverName, serverPort))
    print 'Timestamp: ', datetime.datetime.today()
    print 'Sent: '
    report(request)
    try:
        resPckt, serverAddress = clientSocket.recvfrom(1024)
        break;
    except timeout, to:
        if timeCount < 5:
            timeCount += 1
            print 'Retransmitting ...'
        else:
            clientSocket.close()
            sys.exit('Server ' + str(to) + ' five times.')

response =  struct.unpack('!HHHHHHHH', resPckt)
print 'Timestamp: ', datetime.datetime.today()
print 'Received: ' 
report(response)
clientSocket.close();

# Clent Operation (ix) - Check response
# 0100 0000 0000 0000 <==> 0x4000
# Only the Request/Reponse Flag should be flipped
if (request[0] ^ response[0]) != 0x4000:
    sys.exit('Reponse corrupted: Incorrect message field.')

for i in range(1, 6):
    if (request[i] ^ response[i]) != 0x0:
        sys.exit('Response corrupted: Incorrect message field.')

if computeChecksum(response) != 0xffff:
    sys.exit('Response corrupted: Incorrect checksum.')

if response[7] == 0x8001:
    sys.exit('Server detected a Checksum Error.')
elif response[7] == 0x8002:
    sys.exit('Server detected a Syntax Error.')
elif response[7] == 0x8004:
    sys.exit('Server does not know your social security number.')
elif response[7] == 0x8005:
    sys.exit('Server detected an internal error.')
else:
    print 'Your P.O. Box number: ', response[7]
