import random


#           0       1      2       3       4       5      6        7        8       9
ones =  ["zero", "one",     "two",   "three",     "four",     "five",    "six",    "seven",     "eight",     "nine",
"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# number = 20 #random.randint(0, 99)# input("Enter a number from 0-99: ")

def number_to_phrase(number):
    if number < 20:
        return f"{number}: {ones[number]}"
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        if ones_digit:
            return f"{number}: {tens[tens_digit]}-{ones[ones_digit]}"
        else:
            return f"{number}: {tens[tens_digit]}"
    elif number < 1000:
        hundreds_digit = number // 100
        tens_digit = number % 100 // 10
        ones_digit = number % 10
        under_twenty = number % 100
        if 0 < under_twenty < 20:
            return f"{number}: {ones[hundreds_digit]} hundred and {ones[under_twenty]}"
        elif ones_digit and tens_digit:
            return f"{number}: {ones[hundreds_digit]} hundred and {tens[tens_digit]}-{ones[ones_digit]}"
        elif ones_digit:
            return f"{number}: {ones[hundreds_digit]} hundred and {ones[ones_digit]}"
        elif tens_digit:
            return f"{number}: {ones[hundreds_digit]} hundred and {tens[tens_digit]}"
        else:
            return f"{number}: {ones[hundreds_digit]} hundred"



for i in range(900, 920):
    print(number_to_phrase(i))