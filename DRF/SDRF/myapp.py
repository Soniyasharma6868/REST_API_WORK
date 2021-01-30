#### third party app use for access of api

import requests
URL='http://127.0.0.1:8000/studinfo/'

req=requests.get(url=URL)

data=req.json()

print(data)