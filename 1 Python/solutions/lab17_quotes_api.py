import requests
import json


page = 1
keyword = input("Enter keyword for quote search: ")

def get_quotes(page):
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'

    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    quotes = data['quotes']
    for quote in quotes:
        print(quote['body'])
        print(f"\t--{quote['author']}")

    return data

data = get_quotes(page)

while not(data['last_page']):
    next = input("Do you want to see the next page of results? ").lower()
    if next in ["yes", "yeah", "y", "next"]:
        page += 1
        data = get_quotes(page)
    else:
        break