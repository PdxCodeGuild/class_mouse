import random

while True:
    guesses = 1
    choice = random.randint(1, 10)
    user = None
    while user != choice:

        user = input("Pick a number between 1-10: ")

        while True:
            try:
                user = int(user)
                if user < 1 or user > 10:
                    raise Exception()
                break
            except:
                print("Invalid input")
                user = input("Pick a number between 1-10: ")


        if user < choice:
            guesses += 1
            print("Too low, try again.")
        else:
            guesses += 1
            print("Too high, guess again")
    else:
        print("You guessed correctly!")
        print(f"It took you {guesses} guesses.")

        play_again = input("Would you like to play again? ").lower()
        valid_choices = ["yes", "y", "yeah", "sure", "ok"]
        if play_again not in valid_choices:
            break
        