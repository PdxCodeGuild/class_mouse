x_men = ["storm", "wolverine", "magneto", "juggernaut", "mysterio", "cyclops", "psylocke"]

# for character in x_men:
#     if character == "magneto":
#         index = x_men.find(character)
#         x_men[index] = "Some new character"


# for i in range(len(x_men)):
#     if x_men[i] == "magneto":
#         x_men[i] = "Some new character"

# for i, character in enumerate(x_men):
#     if character == "magneto":
#         x_men[i] = "Some new character"
#     elif character == "wolverine":
#         x_men.remove(character)

# i = 0
# while i < len(x_men):
#     if x_men[i] == "magneto":
#         x_men[i] = "Some new character"
#     elif x_men[i] == "wolverine":
#         x_men.pop(i)
#         # i -= 1
#     i += 1

# x = 0
# while x < 10:
#     if x == 4:
#         print("Im glad its friday")
#         break 


# print(x_men)

# for i in range(20):
#     if i%2 == 1:
#         continue
#     print(i, end=' ')

import string

alphabet = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation

# print(alphabet, numbers, special_characters)


password = "lskdfjsdl"

pw_list = password.split('')
print(pw_list)