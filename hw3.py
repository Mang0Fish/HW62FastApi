#First Section
userId = str(input("Enter id"))
fName = str(input("Enter first name"))
lName = str(input("Enter last name"))
height = float(input("Enter height"))
birthYear = int(input("Enter year of birth"))
print(f"#id:{userId} name:{lName} , {fName} height: {height} year-of-birth: {birthYear}")

#Second Section
grade = int(input("Enter your grade"))
if grade >= 0 and grade <= 40:
    print("try harder next time...")
elif grade >= 41 and grade <= 60:
    print("you're getting there, need some more work")
elif grade >= 61 and grade <= 80:
    print("pretty good")
elif grade >= 81 and grade <= 95:
    print("awesome!")
elif grade >= 96 and grade <= 100:
    print("excellent!!! You're a Star!")
else:
    print("illegal grade")

#Third Section
volume = int(input("Enter volume"))
match volume:
    case 0:
        print("mute")
    case 1 | 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud")

#Fourth Section
sev = int(input("Enter a number"))
if sev % 7 == 0:
    print("seven boom")
else:
    print("not seven boom")

#Fifth Section
fivtre = int(input("Enter a number"))
if fivtre % 5 == 0 and fivtre % 3 != 0:
    print("Fizz")
elif fivtre % 3 == 0 and fivtre % 5 != 0:
    print("Buzz")
elif fivtre % 5 == 0 and fivtre % 3 == 0:
    print("Fizz Buzz")

#Bonus 1
userId1 = str(input("Enter id"))
fName1 = str(input("Enter first name"))
lName1 = str(input("Enter last name"))
height1 = float(input("Enter height"))
birthYear1 = int(input("Enter year of birth"))
userId2 = str(input("Enter id"))
fName2 = str(input("Enter first name"))
lName2 = str(input("Enter last name"))
height2 = float(input("Enter height"))
birthYear2 = int(input("Enter year of birth"))
userId3 = str(input("Enter id"))
fName3 = str(input("Enter first name"))
lName3 = str(input("Enter last name"))
height3 = float(input("Enter height"))
birthYear3 = int(input("Enter year of birth"))
print(f"#id:{userId1:<10} name:{lName1:<10} , {fName1:<10} height: {height1:.2f} year-of-birth: {birthYear1:<10}\n#id:{userId2:<10} name:{lName2:<10} , {fName2:<10} height: {height2:.2f} year-of-birth: {birthYear2:<10}\n#id:{userId3:<10} name:{lName3:<10} , {fName3:<10} height: {height3:.2f} year-of-birth: {birthYear3:<10}")

#Bonus 2
friends = int(input("How many friends came ?"))
pizza = int(input("And how much slices ?"))
print(f"Each friend got {pizza // friends} and {pizza % friends} slices remained")














