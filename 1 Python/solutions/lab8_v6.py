
choices = list(range(0, 1001))

while True:
    try:
        correct_guess = input("Pick a number between 1-1000: ")
        correct_guess = int(correct_guess)
        if correct_guess < 0 or correct_guess > 1000:
            raise Exception()
        break
    except:
        print("Invalid input...")


number_of_guesses = 0

left = choices[0]
right = choices[-1]

while left <= right:
    number_of_guesses += 1
    middle = (left + right) // 2
    if choices[middle] < correct_guess:
        left = middle + 1
    elif choices[middle] > correct_guess:
        right = middle - 1
    else:
        break

print(f"Computer guessed {middle} in {number_of_guesses} tries.")
