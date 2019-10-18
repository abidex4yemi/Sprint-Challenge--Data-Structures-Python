import time
import os
import math
from binary_search_tree import BinarySearchTree

script_directory = os.path.dirname(__file__)

start_time = time.time()

f = open(f"{script_directory}/names_1.txt", 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(f"{script_directory}/names_2.txt", 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
duplicates = []  # (1)
for name_1 in names_1:  # (n)
    for name_2 in names_2:  # (n)
        if name_1 == name_2:  # (1)
            duplicates.append(name_1)  # (1)
# T(n) = 1 + n * n + 1 + 1 => 3n + n^2 => O(n^2)
"""

# Store duplicate string
duplicates = []

# # Pick the first element of names_1 list as starting point
# bst = BinarySearchTree(names_1[0])

# # Cycle over names_1 from position 1
# for i in range(1, len(names_1)):
#     # Insert a new node
#     bst.insert(names_1[i])

# # Cycle over name_2
# for name in names_2:
#     # check if current string node exist in other node
#     if bst.contains(name):
#         # Add duplicate node to duplicate list
#         duplicates.append(name)

# STRETCH: solution


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = int(math.floor((low + high) / 2))

        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle

    return -1


names_1.sort()

for name in names_2:
    found_duplicate = binary_search(names_1, name)
    if found_duplicate:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
