from random import randint
from statistics import mean, median
from string import punctuation
#1
nums = []
for i in range(50):
    nums.append(randint(1,100))

print(list(filter(lambda x: x>50, nums)))
print(list(filter(lambda x: x%7==0, nums)))
print(list(filter(lambda x: 9<x<100, nums)))
print(list(filter(lambda x: x%10 == x//10, nums)))
print(list(filter(lambda x: x%10+x//10 == 9, nums)))
print(list(filter(lambda x: x>mean(nums), nums)))
print(list(filter(lambda x: x>max(nums)/2, nums)))
print(list(filter(lambda x: x>median(nums), nums)))
numsUser = []
for i in range(5):
    numsUser.append(int(input("Enter a num ")))
print(list(filter(lambda x: x not in numsUser, nums)))

def isPrim(num: int):
    prim: bool = True
    if num == 1 or num == -1:
        return False
    for j in range(2, (abs(num))):
        if num % j == 0:
            return False
        else:
            continue
    return True

print(list(filter(lambda x: isPrim(x), nums)))

#2
games =["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print(list(filter(lambda x: len(x) > 8, games)))
print(list(filter(lambda x: x.startswith('F'), games)))
print(list(filter(lambda x: x.count(' ') == 1, games)))
print(list(filter(lambda x: 'v' in x.lower(), games)))
print(list(filter(lambda x: len(x) > 8, games)))

def isPun(s: str):
    for i in s:
        if i in punctuation:
            return True
    return False

print(list(filter(lambda x: isPun(x), games)))
games =[["Grand Theft Auto V", 2013], ["Fortnite", 2017], ["The Elder Scrolls V: Skyrim", 2011], ["Dark Souls", 2011], ["Overwatch", 2016]]
print(list(filter(lambda x: x[1] > 2014, games)))

#3
from random import randint
nums = []
for i in range(20):
    nums.append(randint(-50,50))
print(list(map(lambda x: x**3, nums)))
print(list(map(lambda x: x % 10, nums)))
print(list(map(lambda x: (x*9/5)+32, nums)))
print(list(map(lambda x: 'Positive' if x>0 else 'Negative', nums)))
print(list(map(lambda x: 'Max' if x == max(nums) else 'min' if x == min(nums) else x, nums)))
print(list(map(lambda x: (x % 10)*10 + x//10 if x > 0 else ((x % -10)*-10 + x//-10)*-1, nums)))
print(list(map(lambda x: abs(x), nums)))
sals = [[8000, 2000], [5000, 300], [7000, 10000]]
print(list(map(lambda x: x[0]-x[1], sals)))

#4
fruits = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(list(map(lambda x: x[::-1], fruits)))
print(list(map(lambda x: x[0], fruits)))
print(list(map(lambda x: len(x), fruits)))
print(list(map(lambda x: x[::-1], fruits)))
print(list(map(lambda x: x+'!' if x[-1] == 's' else x, fruits)))
print(list(map(lambda x: x[::-1], fruits)))
fruits = [["Apple", 52], ["Banana", 89], ["Orange", 47], ["Mango", 60], ["Strawberry", 32], ["Pineapple", 50], ["Grapes", 69], ["Watermelon", 30]]
print(list(map(lambda x: x[1], fruits)))
print(list(map(lambda x: x[0]+str(x[1]), fruits)))
print(list(map(lambda x: [x[0]+'!', x[1]] if x[1] > 50 else x, fruits)))

#5
cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(cities, key=lambda x: len(x)))
print(sorted(cities, key=lambda x: x[-1]))
print(sorted(cities, key=lambda x: x[::-1]))
cities = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print(sorted(cities, key=lambda x: x[1]))
print(sorted(cities, key=lambda x: x[1], reverse=True))
print(sorted(cities, key=lambda x: x[2]))
print(sorted(cities, key=lambda x: [x[2], x[1]]))

#global defines a "global" variable that is not confined to the function's scope
#It's not recommended to use global cause then you need to remember the name of the global variable and not use it
#It won't work as the variable changed it value only in the function's scope