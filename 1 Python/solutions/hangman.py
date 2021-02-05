import requests
import random
from hangman_images import hangman_pics

response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_owl/master/1%20Python/data/english.txt')

words = response.text.split('\n')

five_or_more = []

for word in words:
    if len(word) > 5:
        five_or_more.append(word)

rand_word = random.choice(five_or_more)

correct_letters = ['_' for letter in rand_word]

# print(" ".join(correct_letters))

tries = 0
guesses = []
while "".join(correct_letters) != rand_word:
    if tries == 10:
        print("You have no tries remaining")
        print(f"The word was {rand_word}")
        break

    print(hangman_pics[tries])
    print(" ".join(correct_letters))
    print(", ".join(guesses))
    print(f"You have {10 - tries} tries remaining.")

    letter = input("\nGuess a letter: ")
    print(f"You guessed: {letter}")

    if letter not in guesses:
        guesses.append(letter)
        if letter in rand_word:
            for i in range(len(rand_word)):
                if letter == rand_word[i]:
                    correct_letters[i] = letter
        else:
            tries += 1
    else:
        print("You have already made that guess.")
else:
    print(f"Congrats! You guessed {rand_word} in {tries} tries")