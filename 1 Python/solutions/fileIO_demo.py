import time

# file = open('./things/stuff.txt')
# print(file.read())

# file.close()

# with open('./things/stuff.txt', 'r') as file:
#     contents = file.read()

# with open('./things/stuff.txt', 'w') as file:
#     file.write(contents)

# def length(elem):
#     return len(elem)


# while True:
#     name = input("Enter a name: ")

#     if name == 'done':
#         break

#     with open('names.txt', 'a') as file:
#         file.write(name + '\n')


# with open('names.txt', 'r') as f:
#     contents = f.read()

# names = contents.split('\n')
# names.sort(key=lambda e: len(e))


# longest_name = names[0]
# for name in names:
#     if len(name) > len(longest_name):
#         longest_name = name

# print(names[-1])


with open('colors.txt', 'w+') as file:
    colors = "red, blue, yellow, orange"
    file.write(colors)