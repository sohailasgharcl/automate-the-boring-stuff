import random, sys
print("ROCK, SCISSORS, PAPER")
wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print("enter your move: (r)ock (s)cissors (p)aper or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "s" or playerMove=="p":
            break
        print("type one of r,s,p,q")

    if playerMove == "r":
        print("Rock vs ...")
    elif playerMove == "p":
        print("Paper vs ...")
    elif playerMove == "s":
        print("Scissors vs ...")

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print("Rock")
    elif randomNumber == 2:
        computerMove = "p"
        print("Paper")
    elif randomNumber == 3:
        computerMove = "s"
        print("Scissors")

    if playerMove == computerMove:
        print("ties")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("you loss!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("you loss!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("you loss!")
        losses = losses + 1

          
          

