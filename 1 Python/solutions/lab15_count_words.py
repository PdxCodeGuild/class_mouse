import requests

def open_file():
    with open('name of file here', 'r') as file:
        book = file.read()

    return book

def use_requests():
    response = requests.get('book url here')
    
    book = response.text
    return book


def sort_dict(word_dict):
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])


# words = {
#     'banana': 4,
#     'llama': 18,
#     'mouse': 9,
#     'bread': 2
# }

# sort_dict(words)