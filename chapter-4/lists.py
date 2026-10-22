#list data type
print([1,2,3])
print(["cat", "bat", "rat", None, 78, 37])

#list indexes
my_friends = ["Ehsan", "Mujeeb", "Jahangir", "Gulfam"]
print(my_friends[0])
print(my_friends[1])
print(my_friends[2])
print(my_friends[3])
print("hello, " + my_friends[2])

#python will gave you an indexerror when you exceed the index number in the list
#indexes can only be the integers and can never be floats

#multiple lists
spam = [["hamza", "hasham", "sohail"],[10,20,30]]
print(spam[0])
print(spam[1])
print(spam[0][0])
print(spam[1][2])

#negative indexes
spam1 = ["pensil", "pen", "book", "pointer", "bag"]
print(spam1[-1])
print(spam1[-3])
print(spam1[-4])

#slices:getting alist from another list
spam2 = ["swen", "cs", "it", "bba", "ai"]
print(spam2[0:2])
print(spam2[1:4])
print(spam2[0:-1])
print(spam2[:3])
print(spam2[2:])
print(spam2[:])
#getting a list's length
print(len(spam2))

#changing values in list with indexes
spam3 = [9,8,7,6,5,4]
spam3[2] = 56#cannot add string to integer list
print(spam3)
spam3[3] = 90
print(spam3)

spam4 = ["apple","banana","grapes"]
spam4[-1] = "strawberry"
print(spam4)

#list concatenation and replication
print([1,2,3,4] + [5,6,7,8] + ["A","B","C","D"])
print(["laptop", "tablet", "phone"] * 2)

#removing values from list with del statement
spam5 = ["chair", "table", "bed"]
del spam5[2]
print(spam5)

#storing multiple values in a list variable
catNames = []
while True:
    print("enter the name of cat" + str(len(catNames) + 1) + "(or enter nothing to exit):")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print("the names of cats are")
for name in catNames:
    print(" " + name)

#using for loop in lists
supplies = ["pens","staplers","flamethrowers","binders"]
for i in range(len(supplies)):
    print("index " + str(i) + " in supplies is: " + supplies[i])

#the in and not in function
print("sohail" in ["mujeeb","jahangir","danish"])
print("sohail" not in ["mujeeb","jahangir","danish"])

books = ["al-chemist", "peer-e-kamil","deewaniyat"]
print("enter the name of book:")
name = input()
if name not in books:
    print("i don't have this book " + name)
else:
    print("i have book named " + name)

#the multiple assignment trick
a,b,c = 1,2,3
print(a,b,c)

#enamurate functions
friends = ["mujeenba", "ehsana", "jahangira","danisha"]
for index, item in enumerate(friends):
    print("index " + str(index) + " in friends is: " + item)

#using random.choice and random.shuffle functions with list
import random
vegetables = ["tomato", "potato", "colly-flower"]
print(random.choice(vegetables))
random.shuffle(vegetables)#reorders in random sequence 
print(vegetables)

#methods

#finding a vallue in a list with index() method
greetings = ["hey", "hello", "hi", "welcome"]
print(greetings.index("welcome"))

#adding with values with append and insert methods
greetings.append("see you")
print(greetings)#adds value at the end

greetings.insert(2,"love you")
print(greetings)

#removing values from the list with remove method
animals = ["cow", "dog", "goat", "lion"]
animals.remove("goat")
print(animals)

#sorting values with sort() method in the lsit
numbers = [1,7,-3,5,3,9,6]
numbers.sort()
print(numbers)

names = ["ali","danish", "jahangir","ehsan"]
names.sort()
print(names)

name = "faiza"
for i in name:
    print("***" + i + "***")

#tuple data type
grocery_products = ("soap","rice","sugar",23,90)
print(grocery_products)
print(grocery_products[3])
print(grocery_products[1:3])

#converting list and tuple into each other
print(list((1,2,3,"hey")))
print(tuple([1,2,3,4]))

#id function()
print(id("hello"))

#python copy() and deepcopy() function
import copy
spam6 = ['A','B','C','D']
print(id(spam6))
cheese = copy.copy(spam6)
print(id(cheese))
cheese[1] = 'S'
print(spam6)
print(cheese)