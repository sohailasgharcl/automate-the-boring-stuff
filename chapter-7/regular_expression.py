#pattern matching with regular expressions

#creating regex objects
import re
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

#matching regx objects
mo = phoneNumRegex.search("my phone number is 415-455-4242.")
if mo:
    print("phone number found: " + mo.group())
else:
    print("no match found")

#grouping with parantheses
phoneNumRegex1 = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo1 = phoneNumRegex1.search("my phone number is 999-111-2734")
if mo1:
    print(mo1.group(1))
if mo1:
    print(mo1.group(2))
if mo1:
    print(mo1.groups())

#if phone number has parenthesis like (352)-892-2877
phoneNumRegex2 = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo2 = phoneNumRegex2.search("my phone number is (888)-838-1267")
if mo2:
    print(mo2.groups(1))

#matching multiple groups with pipe
heroRegex = re.compile(r"Batman | Tina Fey")
mo3 = heroRegex.search("Batman or Tina Fey")
if mo3:
    print(mo3.group())#it will select the first one

#you can use the prefix first and than write the suffix letters by using pipe
myRegex = re.compile(r"my(school|college|university)")
mo4 = myRegex.search("myschool time was the great time period of my life")
if mo4:
    print(mo4.group())
if mo4:
    print(mo4.group(0))
if mo4:
    print(mo4.group(1))

#optional matching with the question mark
batRegex = re.compile(r"Bat(wo)?man")
mo5 = batRegex.search("The adventures of Batman")
mo6 = batRegex.search("The adventures of  Batwoman")
if mo5:
    print(mo5.group())
if mo6:
    print(mo6.group())

#matching zero or more with the star*
spiderRegex = re.compile(r"spider(wo)*man")
mo7 = spiderRegex.search("I love watching spiderman movies")
mo8 = spiderRegex.search("I love watching spiderwoman movies")
mo9 = spiderRegex.search("I love watching spiderwowowowowowowowoman movies")
if mo7:
    print(mo7.group())#matches one instance
if mo8:
    print(mo8.group())#matches one instance
if mo9:
    print(mo9.group())#matches  eight instances

#matching one or more with  the plus+
antRegex = re.compile(r"ant(wo)+man")
mo10 = antRegex.search("I watch antwoman films")
mo11 = antRegex.search("I watch antwowowowowoman films")
mo12 = antRegex.search("I watch antman films")
if mo10:
    print(mo10.group())
if mo11:
    print(mo11.group())
if mo12:
    print(mo12.group())

#matching specific repetitions
haRegx1 = re.compile(r"(ha){3}")
haRegx2 = re.compile(r"(ha){3,5}")#it's also greedy matching, matches longest possible match
haRegx3 = re.compile(r"(ha){,3}")
mo13 = haRegx1.search("hahaha")
mo14 = haRegx2.search("hahahaha")
mo15 = haRegx3.search("haha")
if mo13:
    print(mo13.group())
if mo14:
    print(mo14.group())
if mo15:
    print(mo15.group())

#greedy vs non-greedy matching
nonGreedyRegx = re.compile(r"(bye){2,6}?")
mo16 = nonGreedyRegx.search("byebyebyebyebye")#it's non-greedy matching , matches the shortest possible version
if mo16:
    print(mo16.group())

#the findall() method 
myphoneRegex = re.compile(r"(\d\d\d\d)-(\d\d\d\d\d\d\d)")#with groups returns a list of tuple of strings
myphoneRegex1 = re.compile(r"\d\d\d\d-\d\d\d\d\d\d\d")#wihtout groups returns a list of string
print(myphoneRegex.findall("home:0328-2728818 office:0302-3748473"))
print(myphoneRegex1.findall("home:0328-2728818 office:0302-3748473"))

#character class
xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall("5 pens, 4 books, 3 pensils, 2 inks"))

#making our own character classes
vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("I love my classmate named faiza very much"))

#lowercase and uppercase matching
caseRegex = re.compile(r"[a-zA-Z]")
print(caseRegex.findall("i am the MOST UGLY BOY in my class."))

#numbers matching
numRegex = re.compile(r"[0-9]")
print(numRegex.findall("24879287914798749287498749128"))

#negative character class
nonVowelRegex = re.compile(r"[^aeiou]")
print(nonVowelRegex.findall("hello , i'll bring a toy for you."))

#caret and dollar signs
beginsWith = re.compile(r"^hello")
print(beginsWith.search("hello, my name is enna bell"))
print(beginsWith.search("he said to me") == None)

endsWith = re.compile(r"\d$")
print(endsWith.search("i have 42"))
print(endsWith.search("i have forty one") == None)

combineRegex = re.compile(r"^\d+$")
print(combineRegex.search("473829498"))

#the wildcard character
dotRegex = re.compile(r".at")
print(dotRegex.findall("the bat at the cat is not flat"))#dot character takes one charater behind the regex

#matching new lines with the dot character
newLineRegex = re.compile(".*",re.DOTALL)
print(newLineRegex.search("be honest\n. do your best\n. get the reward"))

#sub() method to substitute string
namesRegex = re.compile(r"Agent\w+")
print(namesRegex.sub("stephan","Agent hawking gave the documents to Agent steve"))

