from abc import ABC, abstractmethod
import random
import statistics
from typing import override


class NumberArray:
    def __init__(self, size):
        # Initialize array with random numbers
        self._numbers = [random.randint(1, 100) for _ in range(size)]
        self._average = None
        self._std_deviation = None

    # Getters
    @property
    def numbers(self):
        return self._numbers

    @property
    def average(self):
        return self._average

    @property
    def std_deviation(self):
        return self._std_deviation

    # Setters
    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers

    @average.setter
    def average(self, value):
        self._average = value

    @std_deviation.setter
    def std_deviation(self, value):
        self._std_deviation = value


class ArrayHandler(ABC):

    def __init__(self):
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @abstractmethod
    def handle(self, array):
        pass


class ArraySort(ArrayHandler):
    @override
    def handle(self, array):
        """This function can sort the array"""
        sort_choice = input("Sort the array? (yes/no): ").strip().lower()
        if sort_choice == "yes":
            sorted_numbers = sorted(array.numbers)
            array.numbers = sorted_numbers
            print(f"Sorted array: {array.numbers}")
            self.next.handle(array)
        else:
            self.next.handle(array)


class ArrayMult(ArrayHandler):
    @override
    def handle(self, array):
        """This function can multiply the array by a chosen number"""
        multiply_choice = input("Multiply array elements by a number? (yes/no): ").strip().lower()
        if multiply_choice == "yes":
            factor = int(input("Enter the multiplication factor: "))
            multiplied_numbers = [num * factor for num in array.numbers]
            array.numbers = multiplied_numbers
            print(f"Array after multiplication: {array.numbers}")
            self.next.handle(array)
        else:
            self.next.handle(array)


class ArrayAvg(ArrayHandler):
    @override
    def handle(self, array):
        """This function can calculate the arrays average"""
        average_choice = input("Calculate average? (yes/no): ").strip().lower()
        if average_choice == "yes":
            if len(array.numbers) > 1:
                calculated_average = sum(array.numbers) / len(array.numbers)
                array.average = calculated_average
                print(f"Average of numbers: {array.average}")
            else:
                print("Cannot calculate average with less then 2 numbers")
                self.next.handle(array)
        else:
            self.next.handle(array)


class ArrayStd(ArrayHandler):
    @override
    def handle(self, array):
        """This function can calculate the arrays standard deviation"""
        std_choice = input("Calculate standard deviation? (yes/no): ").strip().lower()
        if std_choice == "yes":
            if len(array.numbers) > 1:
                calculated_std = statistics.stdev(array.numbers)
                array.std_deviation = calculated_std
                print(f"Standard deviation: {array.std_deviation}")
            else:
                print("Cannot calculate standard deviation with less than 2 numbers")

            print(f"Final array: {array.numbers}")
            # Display stored statistics
            print("\nStored Statistics:")
            if array.average is not None:
                print(f"Average: {array.average}")
            if array.std_deviation is not None:
                print(f"Standard Deviation: {array.std_deviation}")

        else:
            print(f"Final array: {array.numbers}")

            # Display stored statistics
            print("\nStored Statistics:")
            if array.average is not None:
                print(f"Average: {array.average}")
            if array.std_deviation is not None:
                print(f"Standard Deviation: {array.std_deviation}")


def main():
    array_sort = ArraySort()
    array_mult = ArrayMult()
    array_avg = ArrayAvg()
    array_std = ArrayStd()
    array_sort.next = array_mult
    array_mult.next = array_avg
    array_avg.next = array_std
    array_std.next = None  #To clarify😉
    head = array_sort
    # Create the number array
    size = int(input("Enter the size of the array: "))
    array = NumberArray(size)
    head.handle(array)


if __name__ == "__main__":
    main()













