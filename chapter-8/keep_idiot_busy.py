#importing pyinputplus module as pyip
import pyinputplus as pyip

#create a while loop
while True:
    prompt = "How to keep an idot busy?"
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break#if response equals to 'no' the while clause will end
print("Thank you. Have a nice day!")
