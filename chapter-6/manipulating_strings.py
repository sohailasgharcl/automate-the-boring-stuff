#manipulating strings

#string literals

#double quotes
spam = "I love my friend's GF"
spam1 = "That's the thing I love most"
spam2 = "He is my brother's class mate"
print(spam)
print(spam1)
print(spam2)

#escape characters
my_intro = "i am sohail asghar.\n I love faiza shamshad."
print(my_intro)
me_about_her = "Faiza,If you asked me how many times you came in my mind, I would say once. Because you came, and never left."
print(me_about_her)

#raw string
print(r"I am an undergrad student.\n I am doing my graduation in KFUEIT RYK.")

#multiline strings with triple quotes
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')#multiline stings using triple quotes doesn't ignore spacing or new lines in string

#indexing and slicing strings in python
basic_program  = "Hello, world!"
print(basic_program[8])#index
print(basic_program[5])
print(basic_program[2:])
print(basic_program[:10])
print(basic_program[5:10])#slicing

#the in and not in operator
print("Hello" in basic_program)
print("Hello"  not in basic_program)

#putting strings in another strings
name = "AI"
age = 40000
print("Hello i am " + name + ". I am " + str(age) + " yeras old.")
print("Hello i am  %s.I am %s years old."%(name,age))#str method isn't use to convert integer into string
depart = "ICT"
program = "software engineering"
print("my depart is %s.%s is my program."%(depart,program))

#string methods

#upper() method
first_name = "sohail asghar"
print(first_name.upper())
random_string = "Zepra sings loud now"
print(random_string.upper())

#lower()
print(random_string.lower())
last_name = "MUHAMMAD ASGHAR"
print(last_name.lower())

print("How are you?")
feeling = input()
if feeling.lower() == "great":
    print("I feel great too.")
else:
    print("I hope the rest of your  day is good.")

#islower() method
print(first_name.islower())
print("abc684".islower())
print("879684".islower())

#isupper() method
print("SOHAIL".isupper())
print("SOHAIL_ASGHAR".isupper())
print("KFSHSJFK78932789".isupper())\

#the isX() methods
 
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('    '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

#the startswith() and endswith()
print('Hello, world!'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))

#the join() and split()
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
spliting_string =  '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
print(spliting_string.split('\n'))

#the partition method
print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('world'))
print('Hello, world! I am learning to write program'.partition('XYZ'))
before, sep, after = 'Hello, world!'.partition(' ')
print(before)
print(after)

#Justifying Text with the rjust(), ljust(), and center() Methods
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello, World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20, '='))

#removing whitespaces with the strip(), rstrip(), lstrip() methods
spaam = '    Hello, World    '
print(spaam.strip())
print(spaam.lstrip())
print(spaam.rstrip())

name_intro = 'i am sohail asghar'
for i in name_intro.split():
    print(i[0])