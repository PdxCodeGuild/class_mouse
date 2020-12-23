import random

computer = None
number_of_guesses = 0
while True:
    try:
        correct_guess = input("Pick a number between 1-1000: ")
        correct_guess = int(correct_guess)
        if 0 > correct_guess > 1000:
            raise Exception()
        break
    except:
        print("Invalid input...")

while computer != correct_guess:
    number_of_guesses += 1
    computer = random.randint(1, 1000)

print(f"Computer guessed {computer} in {number_of_guesses} tries.")