import socket
import smtplib
from email.mime.text import MIMEText
import requests
import time

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

def send_email(ip,order) :
	user = ""
	code = "idxbxfcaspfbdjbf"

	reciver = "nats12138@163.com"

	msg = MIMEText("My IP is "+ip+",success after try %s times"%str(order))
	msg["Subject"] = "this is my ip"
	msg["From"] = user
	msg["To"] = reciver

	try :
		smtp = smtplib.SMTP_SSL("smtp.qq.com")
		smtp.login(user, code)
		smtp.sendmail(user, reciver, msg.as_string())
		smtp.quit()
	except Exception :
		print("send fail...")	




time.sleep(20)
sen = requests.session()
for i in range(5) :
	if not test_login(sen) :
		login(sen,i%2)
	else :
		break


ip = getIP()

send_email(ip,i)
