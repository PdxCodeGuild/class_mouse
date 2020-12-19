


# print(not(3 < 4 and True))

# print(not(3 != 4 and False))

# color = "red"

# print("a" < 5)

grade = 85

# print(grade > 80 and grade < 89)
# print(80 < grade < 89)

a = 3
b = 3
c = 3

# print(a == b and b == c) # True
# print(a == b == c) # True
# print((a == b) == c) # False

# letters = "abcdefghijklmnop"

# print('ajk' not in letters)


current_time = input("What time is it? ")

current_time = int(current_time)

# if current_time < 11 and current_time >= 8:
if 8 <= current_time < 11:
    print("Get some coffee")
elif current_time >= 24:
    print("Go to sleep")
# elif 0 < current_time <= 7:
elif 7 >= current_time > 0:
    print("Get some sleep")
elif current_time == 18:
    print("Time to eat!")
else:
    print("Gotta get that bread")