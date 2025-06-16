from statistics import mean
# hw11
# 1
tup1: tuple[int] = (99,)
tup2: tuple[int] = (77, 88, 99)

#tuple for funcs
tup3 = (40, 30, 10, 50, 2, 3, 5, 5, 8, 10, 40, 50)
def tupLen(tup: tuple):
    return len(tup)

def tupSum(tup1: tuple, tup2: tuple):
    return tup1 + tup2

def tupSame(tup1: tuple, tup2: tuple):
    return tuple(i for i in tup1 if i in tup2)

def tupDiff1(tup1: tuple, tup2: tuple):
    return tuple(i for i in tup1 if i not in tup2) + tuple(i for i in tup2 if i not in tup1)


#def tupDiff2(tup1: tuple, tup2: tuple):
#   return tuple(filter(lambda x: x ))

def tupIndex(tup: tuple, index: int):
    try:
        return tup[index]
    except IndexError:
        print("Index out of range")

def tupRev(tup: tuple):
    return tuple(reversed(tup))

def tupMod(tup: tuple, num: int):
    n = 0
    for i in tup:
        if i % num == 0:
            n += 1
    return n

def tupMult(tup: tuple, num: int):
    return tup*num

def tupIndex(tup: tuple):
    return tuple(enumerate(tup))

def tupStats(tup: tuple):
    dictup = {}
    dictup["Max"] = max(tup)
    dictup["Min"] = min(tup)
    dictup["Average"] = mean(tup)
    dictup["Length"] = len(tup)
    dictup["Sorted from big"] = sorted(tup, reverse=True)
    dictup["Sorted from small"] = sorted(tup)
    for i in tup:
        dictup[i] = tup.count(i)
    return dictup

def tupStr(tup: tuple):
    return ''.join(tup)

def tupNoNum(tup: tuple, num: int):
    l = list(tup)
    for i in range(l.count(num)):
        l.remove(num)
    return tuple(l)

#def tupNoRep(tup: tuple):
#    s = set(tup)
#   return tuple(s)

def tupNoRep(tup: tuple):
    l = []
    for i in tup:
        if i not in l:
            l.append(i)
    return tuple(l)
print(tupNoRep(tup3))

def tupNumIndex(tup: tuple, num: int):
    tupN = [i for i,x in enumerate(tup) if x == num]
    return tuple(tupN)

names = []
while True:
    name = input("Enter a name ")
    if name == "done":
        break
    names.append(name)
grades = []
while True:
    grade = int(input("Enter a grade "))
    if grade == -999:
        break
    grades.append(grade)
tupStudents = tuple(zip(names, grades))
print(tupStudents)

# The difference between list and tuple is the mutability, list is mutable while tuple isn't
# The following code doesn't raise an error because it changed a mutable variable inside the tuple,
# the clear function works on all immutable variables
