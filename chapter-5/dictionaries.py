#dictionaries and structuring data
myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
print(myCat)
print("my cat has a " + myCat['color'] + " fur.")

#dictionaries vs lists
spam = ['cats','dogs','moose']
bacon = ['dogs','moose','cats']
print(spam == bacon)

eggs = {'name':'zophie', 'species':'cat', 'age':'8'}
ham = {'species':'cat', 'name':'zophie', 'age':"8"}
print(eggs == ham)#dicts are unordered and cam't be sliced

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
  print('Enter a name: (blank to quit)')
  name = input()
  if name == '':
     break

  if name in birthdays:
     print(birthdays[name] + ' is the birthday of ' + name)
  else:
    print('I do not have birthday information for ' + name)
    print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')

fruits = {"apple":"red","banana":"yellow","grapes":"green"}
for fruit in fruits:
   print(fruits[fruit])#it reresents values

#the keys(), values() and items() methods
spam1 = {'color':'red','age':'2'}
for v in spam1.values():
   print(v)
for k in spam1.keys():
   print(k)
for i in spam1.items():
   print(i)
#to get a list as output
   print(list(i))

#checking wheteher a key or value exists in a dictionary
print("red" in spam1.values())
print("age" in spam1.keys())

#the get() method
print(spam1.get('age',0))
print(spam1.get('number',0))

#the setdefault() method
spam1.setdefault('height',"6'2")
print(spam1)

#pretty printing
import pprint
message = "Faiza, Even if your heart never beats for me, mine has, does, and always will beat for you."
count = {}
for characters in message:
   count.setdefault(characters,0)
   count[characters] = count[characters] + 1
pprint.pprint(count)