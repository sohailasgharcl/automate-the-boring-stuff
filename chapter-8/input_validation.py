#input validationn without PyInputPlus module
while True:
    print("enter your age")
    age = input()
    try:
        age = int(age)
    except:
        print("enter age in digits")
        continue
    if age < 1:
        print("enter age in positive number")
        continue
    break
print(f"your age is {age}")

#the PyInputPlus module
import pyinputplus as pyip
response = pyip.inputNum("enter a number ")
print(response)

#min keyword argument 
response1 = pyip.inputNum("enter a number above six ", min=6)#min keyword argument
print(response1)

#max keyword argument
response2 = pyip.inputNum("enter a number till 8 ", max=8)#max keyword argument
print(response2)

#greaterThan keyword argument 
response3 = pyip.inputNum("enter a number greater than 10 ", greaterThan=10)#greaterThan keyword argument
print(response3)

#lessThan keyword argument
response4 = pyip.inputNum("enter a number less than 11 ", lessThan=11)#lessThan keyword argument
print(response4)

#blank keyword argument
response5 = pyip.inputNum(blank=True)
print(response5,"blank input is allowed")

#limit keyword argument
response6 = pyip.inputNum(limit=3)#after 3 wrong attempts it will raise an error
print(response6)

#timeout keyword argument
response7 = pyip.inputNum(timeout=10)#after 10 seconds it will raise an error
print(response7)

#default keyword argument 
response8 = pyip.inputNum(timeout=10, default='N/A')#after 10 seconds it will print the default value
print(response8)

#allowregexes keyword argument
response9 = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+",r"zero"])
print(response9)

#blockregexes keyword argument
response10 = pyip.inputNum(blockRegexes=[r"[13579]$"])
print(response10)