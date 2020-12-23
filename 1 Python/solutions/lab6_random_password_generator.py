import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

num_lower = int(input("Enter number of lowercase characters: "))
num_upper = int(input("Enter number of uppercase characters: "))
num_numbers = int(input("Enter number of digit characters: "))
num_special = int(input("Enter number of special characters: "))

password = ""
while len(password) < num_lower:
    password += random.choice(lower_case)
while len(password) < num_lower + num_upper:
    password += random.choice(upper_case)
while len(password) < num_lower + num_upper + num_numbers:
    password += random.choice(numbers)
while len(password) < num_lower + num_upper + num_numbers + num_special:
    password += random.choice(special_characters)

password = list(password)
random.shuffle(password)
password = "".join(password)
print(password)