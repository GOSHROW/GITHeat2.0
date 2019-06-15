import smtplib, ssl
import datetime as dt
import time
import requests
from requests.exceptions import HTTPError
from datetime import datetime, date
from datetime import timedelta
import datetime
import time

smtp_server = "smtp.gmail.com"
port = 587 
sender_email = input("Type your sender's email and enter:")
password = input("Type your password and press enter: ")

def send_email():
    message = 'Participate in the ' + name
    server.sendmail(sender_email,input("Enter email id to send to:"),message)
    server.quit()

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() 
    server.starttls(context=context) 
    server.ehlo() 
    server.login(sender_email, password)
except Exception as e:
    print(e)
url='http://codeforces.com/api/'
url+='contest.list'
try:
    response = requests.get(url)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}') 
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    print('Success!\n')
res=response.json()
 
 

id=input("Enter contest id to set reminder for:")
J=0;
for j in range(100):
    if res['result'][j]['id']==id:
        J=j;
        break;
name=res['result'][J]['name']
tym=res['result'][J]['startTimeSeconds']
print(tym, int(time.time()))

time.sleep(tym-int(time.time()))

send_email()
print("EMAIL SENT")
