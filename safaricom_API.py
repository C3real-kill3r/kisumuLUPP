import requests
import json
import base64
from requests.auth import HTTPBasicAuth

consumer_key = "QV7Y55wzhz68RnbHCz2WtABRsjJtCNOr"
consumer_secret = "y12R7o3iYn0yChEg"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

data = r.json()
access_token = "Bearer" + '' + data['access_token']

timestamp = "20180702115427"
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
business_short_code = "174379"

initial_data = business_short_code + passkey + timestamp

password1 = base64.b64encode(initial_data.encode())
password = "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMTE1NDI3"

payload = {
    "Business_short_code": business_short_code,
    "Password": password,
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "10",
    "PartyA": "254703129077",
    "PartyB": business_short_code,
    "PhoneNumber": "254703129077",
    "CallBackURL": "http://mpesa-requestbin.herokuapp.com/zb51eizb",
    "AccountReference": "test",
    "TransactionDesc": "test"
}

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
    }

url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

response = requests.post(url, json=payload, headers=headers)

print (response.text)
