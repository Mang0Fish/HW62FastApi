from array_handler import ArrayHandler
from array_sort import ArraySort
from array_mult import ArrayMult
from array_avg import ArrayAvg
from array_std import ArrayStd
from number_array import NumberArray


def main():
    array_sort = ArraySort()
    array_mult = ArrayMult()
    array_avg = ArrayAvg()
    array_std = ArrayStd()
    array_sort.next = array_mult
    array_mult.next = array_avg
    array_avg.next = array_std
    array_std.next = None
    # To clarify😉
    head = array_sort
    # Create the number array
    size = int(input("Enter the size of the array: "))
    array = NumberArray(size)
    head.handle(array)


if __name__ == "__main__":
    main()
