

# This is the solution
def double_item(arr):
    """This function uses the logic of set operations
    and has the efficiency of o(n/2) as it iterates only half of the list
    (I know that in big o notation there's no such thing, but it's still minimum actions) """
    big_set = set(arr)
    small_set = set()
    for j in range(1, len(arr), 2):
        small_set.add(arr[j])
    return (big_set - small_set).pop()


# This is the bonus second way I solved the question
from collections import Counter


def bonus_double_item(arr):
    """This is just another way I found to solve this question, I don't
    really know what's the efficiency here, but I'm guessing its around o(n)
    but its even shorter in lines, so I added it just for the sake of it"""
    c = Counter(arr)
    return list(c.keys())[list(c.values()).index(1)]


if __name__ == "__main__":
    l1 = [1, 1, 10, 10, 9, 9, 5, 5, 6, 8, 8]
    l2 = [1, 3, 3]
    l3 = [9, 9, 4]
    arr_checking_list = [l1, l2, l3]
    for i in arr_checking_list:
        print(double_item(i))
        print(bonus_double_item(i))
