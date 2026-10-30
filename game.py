import random
import math

while True:
    start = int(input("Enter 1 to start game or 0 to exit it:       "))
    if start == 0:
        break
    elif start == 1:
        choice = int(input("""Welcome To Python Dungeon
You will learn python comparison
operators and some variable types
by multiple choice questions just
enter the choice number 
which one doe you want to learn first 
1)operators
2)variable types"""))
        if choice == 1:
            while True:
                while True:
                    equal_guess = int(input("""Enter the operator for checking
        the equality of two terms or enter 0 to skip the question
        Options:
        1) +
        2) +=
        3) ==
        4) -=:         """))
                    if equal_guess == 0:
                        break
                    elif equal_guess == 3:
                        print ("Ya got that right congrats!")
                        break
                    else:
                        print("Not quite right , retry")
                        continue
                while True:
                    lesser_guess = int(input("""Enter the operator for checking
        the lesserness of an integer or enter 0 to skip the question
        Options:
        1) <
        2) >
        3) <=
        4) >= :      """))
                    if lesser_guess == 0:
                        break
                    elif lesser_guess == 1:
                        print ("Ya got that right congrats!")
                        break
                    else:
                        print("Not quite right , retry")
                        continue
                
                
                while True:
                    greater_guess = int(input("""Enter the operator for checking
        the greaterness of an integer or enter 0 to skip the question
        Options:
        1) <
        2) !>
        3) !<
        4) >  :     """))
                    if greater_guess == 0:
                        break
                    elif greater_guess == 4:
                        print ("Ya got that right congrats!")
                        break
                    else:
                        print("Not quite right , retry")
                        continue
                
                
                while True:
                    inequal_guess = int(input("""Enter the operator for checking
        the inequality of two terms or enter 0 to skip the question
        Options:
        1) ==
        2) !=
        3) +=
        4) -=   :      """))
                    if inequal_guess == 0:
                        break
                    elif inequal_guess == 2:
                        print ("Ya got that right congrats!")
                        break
                    else:
                        print("Not quite right , retry")
                        continue
                break
        elif choice == 2:
            while True:
                while True:
                    var_guess = int(input("""Enter the option which contains
the correct type of this variable \"hello\" or 0 to skip the question
1)int
2)float
3)string
4)nothing  :          """))
                    if var_guess == 0:
                        break
                    elif var_guess == 3:
                        print("You got that right yayayaya")
                        break
                    else:
                        print("You are not quite right, try again")
                while True :
                    var_guess = int(input("""Enter the option which contains
the correct type of this variable \"3\" or 0 to skip the question
1)float
2)int
3)nothing
4)string  :           """))
                    if var_guess == 0:
                        break
                    elif var_guess == 1:
                        print("Ya got it right!")
                        break
                    else:
                        print("Try again")
                while True :
                    var_guess = int(input("""Enter the option which contains
the correct type of variable \"4.5\" or 0 to skip the question
1)UNDEFINED
2)float
3)int
4)string"""))
                    if var_guess == 0:
                        break
                    elif var_guess == 2:
                        print("ya got that right!")
                        break
                    else:
                        print("Retry!!!")
                while True:
                    print("You got everything right or just skipped it " \
"but now you have to pass this final mcq to win")
                    var_guess = int(input("""What is the type of variable of 
\'i love eating pizza\'
Options:
1)UNDEFINED
2)U DONT KNOW
3)int
4)float
5)string
6)line
7)english"""))
                    if var_guess == 5:
                        print("OH WOW YOU GOT THAT RIGHT")
                    elif var_guess == 2:
                        print("THEN PLAY THE WHOLE GAME AGAIN")
                    else:
                        print("You probably skipped every mcq")