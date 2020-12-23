# Problem 1

# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    # i = 0
    # output = ''
    # while i < len(word):
    #     output += word[i] * 2
    #     i += 1
    # return output

    output = ''
    for c in word:
        output += c * 2
    return output



# print(double_letters('hello')) # hheelllloo
# print(double_letters('abc')) # aabbcc


# Problem 2

# Return the number of letter occurances in a string.

def count_letter(letter, word):
    num_string = 0 
    for char in word:
        if letter == char:
            num_string += 1

    return num_string

    # return word.count(letter)


# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2

# Problem 3

# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    # letter = ''
    # for char in word:
    #     if char > letter:
    #         letter = char

    # return letter

    word = list(word)
    word.sort()
    return word[-1]


# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v



# Problem 4

# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    text_count = 0
    while 'hi' in text:
        text_count += 1
        index = text.find('hi')
        text = text[:index] + text[index+1:]

    return text_count

    # return text.count('hi')


# print(count_hi('hihi')) # 2
# print(count_hi('hihihellohihi')) # 4
# print(count_hi('somethinghihello')) # 4

# Problem 5

# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

import string
def snake_case(text):
    text = text.lower()
    text = text.replace(' ', '_')
    for char in text:
        if char in string.punctuation and char != '_':
            text = text.replace(char, '')
    return text



print(snake_case('Hello World!')) # hello_world
print(snake_case('This is another example.')) # this_is_another_example