import requests
from string import punctuation


def use_requests(url):
    response = requests.get(url)
    
    book = response.text
    return book


def sort_dict(word_dict):
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

def count_words(book):
    word_count = {}
    for item in book:
        if item in word_count:
            word_count[item] += 1
        else:
            word_count[item] = 1
    sort_dict(word_count)

def sanitize(url):
    book = use_requests(url)

    start = book.find('*** START OF THE PROJECT GUTENBERG EBOOK AMERICAN PROBLEMS ***') + len('*** START OF THE PROJECT GUTENBERG EBOOK AMERICAN PROBLEMS ***')
    end = book.find('*** END OF THE PROJECT GUTENBERG EBOOK AMERICAN PROBLEMS ***')
    book = book[start:end]
    book = book.translate(str.maketrans('', '', punctuation)).replace('â\x80\x99', "'")

    # for char in punctuation:
    #     book = book.replace(char, " ")
    book = book.lower().split()
    return book

def get_most_common(url):
    book = sanitize(url)
    count_words(book)

def get_pairs(url):
    book = sanitize(url)
    pairs = [f"{book[i]} {book[i+1]}" for i in range(len(book) - 1)]
    count_words(pairs)

def get_chosen_count(url):
    book = sanitize(url)
    word = input("What word do you want to search for? ")
    found_words = [book[i+1] for i in range(len(book) - 1) if book[i] == word]
    count_words(found_words)



def main():
    menu = """
    1) Top 10 most frequent words
    2) Top 10 pairs
    3) Most common following user chosen word
    4) Quit
    """

    url = 'https://www.gutenberg.org/files/64224/64224-0.txt'

    while True:
        choice = input(menu).lower()
        if choice == "4" or choice == "q":
            break
        elif choice == "1":
            get_most_common(url)
        elif choice == "2":
            get_pairs(url)
        elif choice == "3":
            get_chosen_count(url)
            

main()