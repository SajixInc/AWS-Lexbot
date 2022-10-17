import json
import random
import requests
from datetime import datetime

def HealthSummary_Byid(id):


    URL = 'http://staging-api.vivifyhealthcare.com/User/GetAllUserSummary/{}'.format(id)
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNDMyMjkxLCJqdGkiOiJjMjk0NDdlZDE4NDA0N2IxOTBhYzI2MGQ5MDgwZGNiOCIsInVzZXJfaWQiOjV9.TRVn5p3ddUEz0IH3x6ez9QsPQXIXyjPXUywBFUKTPLk'}
    r = requests.get(url = URL,headers=headers)
    data = r.json()['result'][0]["Firstname"]
    date_format = datetime.now()
    date = str(date_format)
    a='Here is ' +data+' s Health Summary generated on ' +date
    return a