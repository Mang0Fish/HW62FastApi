from array_handler import ArrayHandler
from typing import override
import statistics


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
