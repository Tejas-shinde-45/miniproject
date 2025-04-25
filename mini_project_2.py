import random
user_in=input("enter you choice among these :'Rock','Paper','Scissor':-")
com_out=["Rock","Paper","Scissor"]
rn=random.choice(com_out)
print(f"your choice is {user_in} and computers choice is {rn}")

if user_in == rn:
    print("round is tie")
elif user_in =="Rock" and rn=="Paper":
    print("computer Win")
elif user_in =="Scissor" and rn =="Paper":
    print("you Win")
elif user_in =="Rock" and rn=="Scissor":
    print("you win")
elif user_in =="Paper" and rn =="Rock":
    print("you Win")
elif user_in =="Scissor" and rn =="Rock":
    print("computer win")
elif user_in =="Paper" and rn =="Scissor":
    print("computer win")

# print(rn)