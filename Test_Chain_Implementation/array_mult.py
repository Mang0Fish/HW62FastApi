from array_handler import ArrayHandler
from typing import override


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
