


# Problem 1
# Write a function that returns True if the given dictionary has the given key, False otherwise.

def has_key(d, key):
    # if key in d:
    #     return True
    # else:
    #     return False

    # for k in d:
    #     if k == key:
    #         return True
    # return False

    return key in d



# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False


# Problem 2
# Write a function that returns True if the given dictionary is empty, False otherwise.

def is_empty(d):
    # if len(d) == 0:
    #     return True
    # else:
    #     return False

    return len(d) == 0

    # return not(len(d) != 0)

    # return not(d)
    
# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False


# Problem 3
# Write a function that finds and returns the key for the given value, if the value is not in the dictionary, it should return None.

def find_key(d, value):
    
    for key in d:
        if value == d[key]:
            return key
    return None

    # result = [key for key in d if d[key] == value]
    # return result[0] if result else None

    # return [key for key in d if d[key] == value][0] if [key for key in d if d[key] == value] else None


print(find_key({'a': 1, 'b': 2}, 1)) # a
print(find_key({'a': 1, 'b': 2}, 3)) # None