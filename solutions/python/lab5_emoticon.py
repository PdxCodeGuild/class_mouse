import random

eyes = ['一', 'T', '%', '$', '*', '◕', '·', '^']
mouths = ['o', '_', '||', 'x', 'ω', 'ヮ']
sides = [
    ['(', ')'],
    ['[', ']'],
    ['<', '>'],
    ['{', '}'],
    ['/', '\\'],
    ['¯\_', '_/¯']
]

different_eyes = input("Do you want different left/right eyes? ").lower()
go_again = 'yes'
while go_again == "yes":
    num_of_emoticons = ''
    while not(num_of_emoticons.isdigit()):
        num_of_emoticons = input("How many emoticons do you want? ")
    num_of_emoticons = int(num_of_emoticons)

    i = 0
    while i < num_of_emoticons:
        i += 1
        if different_eyes == 'yes':
            left_eye = random.choice(eyes)
            right_eye = random.choice(eyes)
        else:
            random_eyes = random.choice(eyes)
            left_eye = random_eyes
            right_eye = random_eyes
        random_mouth = random.choice(mouths)
        random_side = random.choice(sides)

        face = random_side[0] + left_eye + random_mouth + right_eye + random_side[1]
        print(face)

    go_again = input("Do you want to generate more? ").lower()
