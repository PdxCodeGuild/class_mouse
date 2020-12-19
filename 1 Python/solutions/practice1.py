
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

    # while a != 1 and a !=0:
    #     a //= 2
    #     if a == 0:
    #         return True
    #     elif a == 1:
    #         return False


# print(is_even(5)) # False
# print(is_even(6)) # True
# print(is_even('hello'))


# Write a function that takes two integers, a and b, and returns 
# True if one is positive and the other is negative, and return False otherwise.

def opposite(a, b):
    if a > 0 and b < 0:
        return True
    elif a < 0 and b > 0:
        return True
    else:
        return False

# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False
# print(opposite(0, 5))


# Write a function that returns True if a number within 10 of 100.
def near_100(num):
    # if 90 <= num <= 110:
    #     return True
    # else:
    #     return False
    
    if num in range(90, 111):
        return True
    else:
        return False



# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Write a function that returns the maximum of 3 parameters.
def maximum_of_three(a, b, c):
    # return max(a, b, c)
    # if a > b:
    #     if a > c:
    #         return a
    #     else:
    #         return c
    # elif b > a:
    #     if b > c:
    #         return b
    #     else:
    #         return c
    # else:
    #     if a > c:
    #         return a
    #     else:
    #         return c
    numbers = [a, b, c]
    numbers.sort()
    return numbers[-1]

# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10
# print(maximum_of_three(4, 4, 8))

# Write a loop to print the powers of 2 from 2^0 to 2^20
def print_powers_2():
    # num = 0
    # while num < 21:
    #     num +=1

    for num in range(0, 21):
        if num == 20:
            print(2 ** num)
        else:
            print(2 ** num, end=", ")

print_powers_2() # 1, 2, 4, 8, 16, 32, ...