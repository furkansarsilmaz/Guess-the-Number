import random
import time

def Guess_Number():
    """
the computer randomly selects a number between 0 and 9, and the player has 3 chances to guess it.
The game provides feedback after each guess, letting the player know if the guess was too high or too low.
If the player guesses correctly, they win and are given the option to play again. If all chances are used up,
the game ends with an option to retry.
    
    """
    print("Welcome to the Game !!!")
    time.sleep(1)
    print("Number has been generated ! ")
    number = random.randint(0,9)
    #print(number)

    time.sleep(1)
    chance = 3
    while chance > 0 :
        try:
            Guess = int(input("Guess the number (0-9) : "))
            if Guess < number :
                print("Number is Greater Than Guess")
                chance -= 1
                print(f"You have {chance} chances left")
            elif Guess > number :
                print("Number is lower than Guess")
                chance -= 1
                print(f"You have {chance} chances left")
            else:
                print("You Won !")
                try:
                    Retry = str(input("Do you want to play again (Y/n) :")).lower()
                    if Retry == "y":
                        Guess_Number()
                    else:
                        print("Goodbye !")
                        break
                except ValueError:
                    print("Y or N please")


        except ValueError:
            print("Please give a number")
            chance -= 1
            print(f"You have {chance} chances left")

    if chance == 0 :
        print("You lose.")
        try:
            Retry = str(input("Do you want to play again (Y/n) :")).lower()
            if Retry == "y":
                Guess_Number()
            else:
                print("Goodbye !")
        except ValueError:
            print("Y or N please")        
Guess_Number()