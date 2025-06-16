import pandas as pd
import numpy as np
"""
df = pd.DataFrame({'A':[None, 2, 3, None, 5], 'B':[10, None, None, 40, 50], 'C':[100, None, 300, 400, None]})
print(df)
df.dropna()
df.dropna(thresh=1)
print(df.dropna(subset = ['A','C']))
print(df.fillna('55'))
print(df.fillna())"""

# from Customer import Customer
#
# c1 = Customer(6, 'Ali', 'Baba', 'Persia', '501234567')
#
# #print(repr(c1))
# exec("c2 = Customer(6, 'Ali', 'Baba', 'Persia', '501234567')")
# #print(c2)
#
# c3 = eval(repr(c1))
# print(c3)


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#     def __repr__(self):
#         return f"{self.val}"
#
#
#
#
# root = [4, 2, 7, 1, 3, 6, 9]
# trees = []
# for i in range(len(root) - 2):
#     trees.append(TreeNode(root[i], root[i + 1], root[i+2]))
#
# print(trees)
#
#
# def invertTree(node):
#     if not node:
#         return None
#     leftInverted = invertTree(node.left)
#     rightInverted = invertTree(node.right)
#     node.left = rightInverted
#     node.right = leftInverted
#     return root

# l = [2, 5, 2, 6, 34, 2, 4, 7, 4, 5]
#
# g = lambda x: x if x % 2 == 0 else 0
# print(g(l))


import numpy as np
import time
from memory_profiler import profile


def light_computation(size=1000):
    """This function doesn't use much memory."""
    result = 0
    for i in range(size):
        result += i * 2
    return result


def create_small_list(size=1000):
    """This function creates a reasonably small list."""
    return [i ** 2 for i in range(size)]


def calc_log_function(size=100000000):
    """This function creates a large NumPy array in memory."""
    # Create a large array
    large_array = np.random.random((size,))
    # Do some operations on it
    processed = large_array * 2
    transformed = np.log(processed + 1)
    # Simulate some processing time
    time.sleep(1)
    return transformed


def another_function(n=10):
    """Another function that doesn't use much memory."""
    return {i: i ** 3 for i in range(n)}


@profile
def main_processing_function():
    """Main function that calls all other functions."""
    print("Starting processing...")

    # Call the light computation
    result1 = light_computation(2000)
    print(f"Light computation result: {result1}")

    # Call the small list creation
    small_list = create_small_list(3000)
    print(f"Small list first 5 elements: {small_list[:5]}")

    # Call the memory heavy function
    heavy_result = calc_log_function()
    print(f"Heavy function result: {heavy_result}")

    # Call another light function
    light_result = another_function(15)
    print(f"Another light function result size: {len(light_result)}")

    print("Processing complete!")
    return "Success"


main_processing_function()















