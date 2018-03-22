import socket
import requests

def getIP() :
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	try :
		s.connect(("baidu.com",12567))
		ip = s.getsockname()[0]
		s.close()
	except Exception :
		ip = "N/A"

	return ip

def test_login(se) :
    try :
        content = se.get("http://baidu.com",timeout=1)
        if "baidu" in content.text :
            return True
        else :
            return False
    except :
        return False
def login(se,second=True) :
	postd = {"DDDDD":"",
	         "upass":"",
	         "0MKKey":""}
	
	postd1 = {"DDDDD":"",
	         "upass":"",
	         "0MKKey":""}

	login_url = "http://10.3.8.211/"
	if second :
		data = sen.post(login_url,postd)
	else :
		data = sen.post(login_url,postd1)


sen = requests.session()

for i in range(5) :
	if test_login(sen) :
		break
	else :
		login(sen,i%2)
if test_login(sen) :
	print("login success after %s times"%i,"ip is",getIP())
else :
	print("login fail")
