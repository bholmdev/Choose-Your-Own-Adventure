name = input("Welcome to insert book name here.  What is your name?\n")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.  Which whay would you like to go?")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across.  Type 'walk' to walk around it or 'swim' to swim across it.")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")
    else:
        print("Not a valid option.  You lose.")
elif answer == "right":
    answer = input("You come to a bride, it looks wobbly.  Do you want to cross it or head back?  Type 'cross' to cross the bridge, type 'back' to head back.")
    if answer == "back":
        print("You go back and lose.")
    if answer == "cross":
        answer = input("You cross the bridge and encounter a stranger.  Do you talk to them?  Type 'yes' or 'no'.")
        if answer == "yes":
            print("The stranger greets you, and you win.")
        elif answer == "no":
            print("The stranger is offended and kills you.  You are dead.")
        else:
            print("Not a valid option.  You lose.")
else:
    print("Not a valid option.  You lose.") 
