


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


# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None


# Problem 4
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

def reverse_dict(d):
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key

    # for key in d:
    #     new_dict[d[key]] = key

    return new_dict

    # return {d[key]: key for key in d}


# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}

# Problem 5
# Write a function that merges two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

def merge(list1, list2):
    merged_dict = {}
    for index in range(len(list1)):
        # merged_dict[list1[index]] = list2[index]
        merged_dict.update({list1[index]: list2[index]})

    return merged_dict

    # return {list1[index]: list2[index] for index in range(len(list1))}

# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}

# Problem 6
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    new_dict = {}
    for d_index in d:
        if d[d_index] > 10:
            new_dict[d_index] = d[d_index]

    return new_dict

# print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) # {'b': 15, 'c': 12}