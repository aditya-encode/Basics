import random
print("i am thinking about the number from 1 to 20")
gg1=random.randint(1,20)

for i in range (1,7):
    if i ==6:
        print("please type your number")
        gg= int(input())
        if gg ==gg1:
          print("congratulation,u guessed it right")
        else:
            print("you missed to guess the correct number and the correct number was ",gg1)
    else:

        print("please type your number")
        gg= int(input())
        if gg < gg1:
            print("the number is too low")
        elif gg > gg1 :
            print("the number is too high")
        else:
            print("congratulation,u guessed it right")
            break

