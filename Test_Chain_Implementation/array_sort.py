from array_handler import ArrayHandler
from typing import override


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
