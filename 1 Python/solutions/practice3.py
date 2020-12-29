import random

# Problem 1
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

def random_element(a):
    num = random.randint(0, len(a) - 1)
    return a[num]


# print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'
# print(random_element(['apples', 'bananas', 'pears', 'pecans', 'avocado']))

# Problem 2
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
def eveneven(llama):
    counter = 0
    for num in llama:
        if num % 2 == 0:
            counter += 1

    return counter % 2 == 0

# print(eveneven([5, 6, 2])) # True
# print(eveneven([5, 5, 2, 4])) # False

# Problem 3
# Write a function that returns the reverse of a list.

def reverse(panda):
    # panda.reverse()
    # return panda

    return panda[::-1]

    # panda.sort(reverse=True)
    # return panda

    # reversed_panda = []
    # while len(panda) > 0:
    #     reversed_panda.append(panda.pop())

    # return reversed_panda

# print(reverse([1, 2, 3])) # 3, 2, 1
# print(reverse([4, 22, 1])) # 1, 22, 4

# Problem 4
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    less_than_ten = []
    for num in nums:
        if num < 10:
            less_than_ten.append(num)
    return less_than_ten

    # return [num for num in nums if num < 10]


# print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]


# Problem 5
# Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
    # output = []
    # for num in nums1:
    #     if num in nums2:
    #         output.append(num)
    # return output

    return [num for num in nums1 if num in nums2]


# print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]

def common_elements3(nums1, nums2, nums3):
    # output = []
    # for num in nums1:
    #     if num in nums2 and num in nums3:
    #         output.append(num)
    # return output

    return [num for num in nums1 if num in nums2 and num in nums3]


# print(common_elements3([1, 2, 3], [2, 3, 4], [3, 4, 5, 6])) # [3]


# Problem 6
# Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):
    # output = []
    # for index in range(len(nums1)):
    #     output.append(nums1[index])
    #     output.append(nums2[index])
    # return output

    # return [(nums1[i], nums2[i]) for i in range(len(nums1))]

    return [num for num in (nums1, nums2) for num in nums2]


print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]