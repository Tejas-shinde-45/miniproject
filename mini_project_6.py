

# _________________________________________________Mini Project game_____________________________________________________
# Project Idea: "Code Quest: Logic Puzzle Adventure"
# A text-based logic puzzle adventure game made entirely using conditionals, loops, and functions.

# It’s like a "choose-your-path" story mixed with brain teasers and coding challenges — all in the terminal, all logic-based.

# Players (your students) move through stages of a fictional world.
# At each stage, they must solve puzzles using logic, math, or reasoning, implemented as Python functions.

# Expected output:

# 🧭 Welcome, Adventurer!

# You're trapped in a logic dungeon.
# Solve puzzles to unlock the next gate!

# Level 1: The Number Gate
# > Enter a number divisible by 3 and 5 but not 10:

# Level 2: The Code Wall
# > Crack the passcode: it's the reverse of '3142', doubled.

# Level 3: The Word Riddle
# > Find the word with 3 vowels and ends with 'ing':

# Level 4: The Loop Maze
# > Reach 100 by adding only even numbers from 1–20. How many steps?



username=input("Create the username:")
password=input("Create the password:")

if len(password)<6:
    print("password must be have 6 or more charachter:")
elif password.isdigit() and password.isaplpha():
    print("your password is strong")
else:
    print("password create a sucessfully::")

    print("Login please")

    user=input("enter your username:")
    passe=input("enter your password:")

    if user==username and passe == password:
        print("logint successfully")


        print("WELCOME TO ADVENTURE😉")


        print("LEVEL 1")
        num=int(input("enter the number which is divisible by 3,5 but not 10"))        
        if num % 3==0 and num%5==0 and num%10 !=0:
            print("congratulations you pass this level 1")

            print("Level 2")
            print("password cracker number which is reverse of user input and double so guess it ")
            num1=input("enter the number:")
            num0=str(num1)
            num_rev=int(num0[::-1])
            num_duble=num_rev * 2
            num2=int(input("enter the password:"))
            if num2==num_duble:
                print("congratulation you are correct")
            else:
                print("you are wrong try again")          
            

        else:
            print("Condition not satisfied.")
    else:
        print("you enter the wrong answer")


        # print("Level 3")
            # word=input("enter the word:")
            # vowels=['a','e','i','o','u']