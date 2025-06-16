from array_handler import ArrayHandler
from typing import override


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
