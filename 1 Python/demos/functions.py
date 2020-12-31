


def pretty_print(message="Hello", name="Leslie"):
    print(f"{message} {name}")


def add(num, num2):
    num3 = num + num2
    counter = 0
    while counter < 1000:
        counter += 1
    return counter, num3

count, result = add(3, 4)
print(result)
print(count)



# greeting = "Hello"
# name = "Bob"
# pretty_print(name=greeting, message="Howdy")
