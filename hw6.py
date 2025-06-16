# Section 1
import copy
import statistics
import random

numbers: list[int] = []
i = 0
num = 80
for index in range(20):
    numbers.append(num)
    num += 1
    i += 1
print(numbers[0], numbers[-1], len(numbers), numbers[3:12], numbers[3:], numbers[:9])
numbers.insert(len(numbers) // 2, 999)
print(numbers[-1::-1], numbers[1::2])

# Section 2
temps: list[float] = []
while True:
    temp = float(input("Enter a temperature"))
    if temp == -999:
        break
    elif -50 <= temp <= 50:
        temps.append(temp)
temps.extend([-20.0, 39.1, 18.5])
print(max(temps), min(temps), sum(temps) / len(temps), statistics.mean(temps))
del temps[0]
temps.remove(18.5)
tempLast = temps.pop()
print(temps)
copy.copy(temps).sort()
copy.copy(temps).sort(reverse=True)
# Sorted creates a new sorted list, sort modifies the original list
# Reversed returns an object

# Section 3
bools: list[bool] = []
i = 0
while i < 3:
    bools.append(random.choice([True, False]))
    i += 1
print("The list only contains trues" if all(bools) else "The list doesn't contain only trues")
print("The list at least contains one true" if any(bools) else "The list doesn't contain a true")
print("The list doesn't contain only falses" if any(bools) else "The list only contains falses")
print("The list doesn't contain a false" if all(bools) else "The list at least contains one false")
print(bools)
randomNums: list[int] = []
for index in range(5):
    randomNums.append(random.choice([-2, -1, 0, 1, 2]))

print("The list contain zeroes" if 0 in randomNums else "The list doesn't contain zeroes")
print("The list is not only zeroes" if [-2, -1, 1, 2] in randomNums else "the list is only zeroes")
print(randomNums)

# Section 4
numbers2: list[int] = [index for index in range(95, 106)]
numbersEven: list[int] = [index for index in range(10, 21, 2)]
randomBools: list[bool] = [random.choice([True, False]) for index in range(5)]
# You need to use _ when the variable description is long and you want it to be understandable
randomNums2: list[int] = [random.choice(range(1, 100)) for index in range(10)]
bigRandomNums2: list[int] = [index for index in randomNums2 if index > 50]
bigRandomNums2 = [index for index in [random.choice(range(1, 100)) for _ in range(10)] if index > 50]
word = input("Enter some strings")
words: list[str] = [index for index in word if index != 't' and index != ' ']

# Section 5
numbers3: list[int] = [random.choice(range(1, 10)) for index in range(4)]
while True:
    x = input("Enter an index")
    if x == -999:
        break
    try:
        print(numbers3[int(x)])
    except IndexError:
        print("The index you entered is out of range")
    except Exception as e:
        print("You need to enter an int")
