import requests
from requests.exceptions import HTTPError

usrmthd='user.info?handles='

usrkey={'handle','firstName','lastName','country','city','rating','maxRating','friendOfCount','avatar','contribution','organization','rank'}

url='http://codeforces.com/api/'
 
url+=usrmthd+input("Enter the username:")

for i in range(1000):
    ch=input("Enter Y to input more names(<1000), any other to exit:")
    if ch!='Y'and ch!='y':
        break
    url+=";"+input("Enter the username:")
n=i

try:
    response = requests.get(url)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}') 
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    print('Success!\n')

res=response.json()

for j in range(n+1):
    for i in usrkey:
        if res["result"][j][i]:
            print((i.upper()+":{}").format({res['result'][j][i]}))
    print("\n")