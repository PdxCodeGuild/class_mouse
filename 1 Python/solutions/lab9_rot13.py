import string

available_characters = string.printable

user_string = input("Enter the message to be encrypted: ")
rotation = int(input("Enter the amount to be rotated: "))

output = ""
for char in user_string:
    if char in available_characters:
        # Get the index and add 13
        index = available_characters.find(char) # + 13
        index += rotation

        output += available_characters[index % len(available_characters)]
    else:
        output += char

print(f"{user_string} encrypted to: {output}")