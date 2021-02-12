import requests

response = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en')
print(response)