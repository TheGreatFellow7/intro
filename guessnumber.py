import random

computer_sel=random.randint(1,50)
guess_limit=8
print("Player has only ",guess_limit," chances to guess")

while(guess_limit!=0):
    user_guess=int(input("Guess number between 1 to 50"))
    if computer_sel==user_guess:
        print("Congratulations you guessed the correct number in ",guess_limit, "chances")
        break
    elif computer_sel-user_guess < 5:
        guess_limit-=1
        print("Ohh you missed it but you are too close to the correct number")
        print("Hurry you have ",guess_limit," chances left")
    else:
        guess_limit-=1
        print("You are too far from the correct number")
        print("Hurry you have ",guess_limit," chances left")
if(guess_limit==0):
            print("Sorry you ran out of the chances")
