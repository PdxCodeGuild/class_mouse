import requests

def get_book(url):
    response = requests.get(url)
    return response.text

def get_title(book):
    lines = book.split('\n')
    for line in lines:
        if "Title: " in line:
            return line[7:]

def main():
    url = 'https://www.gutenberg.org/files/64224/64224-0.txt'
    book = get_book(url)
    title = get_title(book)

    print(title)

main()