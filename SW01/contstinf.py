import requests
from requests.exceptions import HTTPError
from datetime import datetime, date
from datetime import timedelta
import datetime
import time

cntstmthd='contest.list'

cntstkey={'id', 'name'}

url='http://codeforces.com/api/'
 
url+=cntstmthd

try:
    response = requests.get(url)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}') 
except Exception as err:
    print(f'Other error occurred: {err}')  
else:
    print('Success!\n')

res=response.json()

maxactvcontst=100
now=datetime.datetime.now().timestamp()
t1 = timedelta(seconds = now)

for j in range(maxactvcontst):
    if res['result'][j]['phase']=='BEFORE' and res['result'][j]['frozen']==False:        
        for i in cntstkey:
            if res["result"][j][i]:
                print((i.upper()+":{}").format(res['result'][j][i]))
        print('DURATION HOURS:{}'.format(res['result'][j]['durationSeconds']/3600))
        startt=res['result'][j]['startTimeSeconds']
        print('START TIME:{}'.format(time.ctime(startt)))
        t2 = timedelta(seconds = res['result'][j]['startTimeSeconds'])
        t3 = t2 - t1
        print('TIME LEFT:{}\n'.format(t3))