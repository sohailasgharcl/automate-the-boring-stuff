import random
real_number = random.randint(0,10)
print("I am thinking a number between 0 and 10")

for i in range(10):
    print("take a guess.")
    guess_number = int(input())

    if guess_number > real_number:
        print("your guess is too high")
    elif guess_number < real_number:
        print("your guess is too short")
    else:
        break
if guess_number == real_number:
    print("you successfully guessed the correct number.")
else:
    print("Try Try agian untill success.")