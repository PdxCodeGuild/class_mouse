# print("hello", end="-")
# print("world")

# print('banana', 'orange', 'apple')

# x = 5
# y = 'something'
# z = True

# print(x, y, z, sep=":)")

# color = input("What is your favorite color? ")
# print(f"I like {color} too!")


# greeting = "HELLO EVERYONE!!"

# greeting = greeting.lower()

# print(greeting)


# i = 0
# while i < 100:
#     print(i%5)
#     i = i + 1

# print(r'\t hello \n there \\')



greeting = "Welcome class mouse!"

print(len(greeting))

# print(greeting[1:10:-1])

# print(greeting.replace('mouse', 'tiger'))
print(greeting.replace('s', ''))
# print(greeting.strip('W'))

split_greeting = greeting.split('s')
print(split_greeting)

joined_greeting = "s".join(split_greeting)
print(joined_greeting)

for char in greeting:
    print(char, end="")
