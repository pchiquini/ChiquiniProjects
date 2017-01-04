###############################################################
			CS356 - Lab 1
###############################################################

Name: Patrizio Chiquini
UTEID: pc22566


Excersice O Output:

---------------------------------------------------------------
Client IP address/Port number: 128.83.130.18-38588
----------------------------------------
[Client -> CS356 Server] Request
[0-3] 01 64 01 07
[4-7] 64 71 9C 29
[8-11] 00 00 00 2E
[12-15] 50 62 00 00

Error: Checksum verification failed!
----------------------------------------
[CS356 Server -> Client] Type 0 Response
[0-3] 41 64 01 07
[4-7] 64 71 9C 29
[8-11] 00 00 00 2E
[12-15] 3C CA 80 01


Excersice 1 Output: NOT AVAILABLE
---------------------------------------------------------------
THIS IS WHAT IT SHOULD HAVE BEEN

Client IP address/Port number: 128.83.130.17-44173
----------------------------------------
[Client -> CS356 Server] Request
[0-3] 81 64 01 07
[4-7] 00 00 00 03
[8-11] 80 53 82 11
[12-15] F0 1B 8B 10

Received: Type 1 Request

Server Under Test (SUT) IP-Port: 128.83.130.17-35600
----------------------------------------
[CS356 Server -> SUT] Type 0 Request
[0-3] 01 64 01 07
[4-7] 6B 7B 45 67
[8-11] 00 00 00 00
[12-15] 4C B2 00 00
----------------------------------------
[SUT -> CS356 Server] Type 0 Response
[0-3] 81 64 01 07
[4-7] 6B 7B 45 67
[8-11] 00 00 00 00
[12-15] 4C CB 80 04
----------------------------------------
[CS356 Server -> Client] Type 1 Response
[0-3] C1 64 01 07
[4-7] 00 00 00 03
[8-11] 80 53 82 11
[12-15] 3B 2C 00 00
Type 0 transaction SUCCESS.  P.O. Box number is:  4

Extra Notes:
---------------------------------------------------------------
Even though the outcomes of the project might not show it, I started worked on the project a week in advance with at least 3-4 hours of work put into it every day. However, I honeslty don't know why I struggled so much with this. I spent a majority of time figuring out bit manipulation and, unfortunately, I kept changing the approach which only made me more confused and scattered. 
I personally feel that my lack experience with Python made me focus on langugage more instead of the main concept of the project itself. (Keep in mind this is my first time doing Python). 

All the proper code and syntax is present, but the failure to get checksum to work properply created a domino effect that did not allowed me to even start on the additional files properly. 

There was definitely a lot of work put into this but, unfortunately, my work on this project was not enough. I hope that I will be able to receive some minor points for completion, syntax, structure, and concept understanding. 

