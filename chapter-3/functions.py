#helloFunc 
def hello():
    print("Hello,World")
    print("Hello,Mujeeb")
    print("Hello,Ehsan")
hello()

#def statement with params and arguments
def hello_1(name):
    print("Hello," + name)
hello_1("Jahangir")#return value

def sum(a,b):
    sum = a + b
    print(sum)
sum(29,15)#return value

#return value and return statement
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidely so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

spam1 = print("hello!")
print(None == spam1)

#keyword arguments
print("hello", end="")
print("world")
print("mujeeb", "ehsan","jahangir", sep=",")

#the call stack in functions
def a():
    print("a() starts")
    b()
    d()
    print("a() ends")
def b():
    print("b() starts")
    c()
    print("b() ends")
def c():
    print("c() starts")
    print("c() ends")
def d():
    print("d() starts")
    print("d() ends")
a()

#local variables cannot be used in global scope
def var():
    eggs = 8698
    print(eggs)
var()
#print(eggs)causes error because local variables cannot be used in global scope

#local scope cannot use variables in another local scope

def myLocal():
    chairs = 90
    local_second()
    print(chairs)
def local_second():
    tables = 36
    chairs = 78
myLocal()

#call stack

def local_scope():
    tomato = 89
    another_local_scope()
    print(tomato)
def another_local_scope():
    potato = 67
    print(potato)
    #tomato = 23
local_scope()

#global variables can be read from local scope

def local_one():
    print(books)
books = 34
#local_one()
print(books)

#local and global variables with the same name

def outer():
    pens = "outer local"
    print(pens)
def inner():
    pens = "inner local"
    print(pens)
    outer()
    print(pens)
pens = "global"
inner()
print(pens)

#global statement

def spam():
    global eggs
    eggs = "spam"
spam()
print(eggs)

#expection handling 
def spam2(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("error: invalid arguments")#when we use return statement we print it using print()
print(spam2(2))
print(spam2(12))
print(spam2(0))
print(spam2(1))