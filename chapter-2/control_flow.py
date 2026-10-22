#boolen values

spam = True
print(spam)

#comparison operators

print(42 == 42)
print(42 == 92)
print(2 != 3)
print(67 != 67)
print(47 >= 40)
print(47 >= 46)
print( 90 <= 100)
print(6 <= 10)
print(48 > 21)
print(48 > 61)
print(78 < 97)
print(78 < 972)
print("hello" == "hello")
print("world" == "World")
print("dog" != "cat")
print(True == True)
print(True != False)
print(42 == 42.0)
print(42 == "42")

#boolean operators

print(True and True)
print(True  and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

#mixing boolean and comparison operators

print((4>3) and (9<10))
print((4>3) and (90>100))
print((4>3) or (90<10))
print((4>38) or (9<10))

#block of codes 
username = "Ehsan"
password = "456789"
if username == "Ehsan":
    print("Ehsan you are welomed.")
    if password == "456789":
        print("access granted.")
    else:
        print("username or password is incorrect")

#flow control statements

#is statement
if (47 < 50):
    print("condition is True.")

depart = "SWEN"
if depart == "SWEN":
    print("I like SWEN.")

#if and else
cast = "sindhi"
if cast == "Baloch":
    print("Baloch are very barve people.")
else:
    print("these people are very coward.")

if (2 > 5):
    print("condition is true.")
else:
    print("condition is false.")
# if and elif statements
age = 27
if age == 90:
    print("you are a great grand father.")
elif age <= 30:
    print("you are young.")

name_of_steduent = "Naseer"
depart_of_student = "AI"
if name_of_steduent == "Ali":
    print("You belong to BBA depart.")
elif depart_of_student == "AI":
    print("You are Naseer and your depoart is AI.")
elif depart_of_student == "CS":
    print("You are  not Ali , may be you are Adnan.")
else:
    print("you are stranger.")

#while loop statement

spam = 0
while spam < 5:
    print("hello, world")
    spam = spam + 1

name = ""
while name != "yourname":
    print("please type your name.")
    name = input()
print("thank you!")

while True:
    print("please type your name.")
    name = input()
    if name == "sohail":
        break
print("verified")

while True:
    print("type your subject.")
    subject = input()
    if subject != "SQE":
        continue
    print("course, SQE is registered. Now enter other course for registration. ")
    second_subject = input()
    if second_subject == "PDC":
        break
print("registration successfully completed") 

#for loop
for i in range(5):
    print("I am sohail asghar.")

sum = 0
for i in range(0,101):
    sum = sum + i
print(sum)

#the starting, stopping and stepping arguments to range()
for i in range(0,20,4):
    print(i)
for i in range(50,-10,-10):
    print(i)

#importing modules

import random
for i in range(5):
    print(random.randint(0,20))

import sys
while True:
    print("type exit to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed" + response + '.')
    