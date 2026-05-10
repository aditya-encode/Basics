import random,sys
print("lets play rock-paper and scisssor game")
wins = 0
loss=0
tied=0
while True :                            #if we have not used while loop it will only take one input and stop the execution so to run game again and again,we used whikle loop
    print("%s wins,%s loss,%s tied"%( wins, loss, tied))
    print("input (R)ock,(P)aper,(S)cissor, (Q)uit")
    player_move=input().lower()  #user R type kare to and compter r runkare to rock vs rock thatu pan match tied natu avtu kem ke R!=r thatu hatu etle

    if player_move=='q' or player_move=='Q':  #'r' ma lakhvu direct r na lakhvuu nai to function k variable smji lese  and define nai karya etle error batavse
        print("thanks u for  trying the game")
        sys.exit() 
    elif player_move=='S' or player_move=='s':
        print("scissor  versus ")
    elif player_move=='P' or player_move=='p':
        print("paper versus") 
    elif player_move=='R' or player_move=='r':
        print("rock versus")
    else:
        print("please enter valid input")
        continue  #if user input invalid thing the execution will start again
    computer_move=random.randint(1,3)
    if computer_move==1:
        computer_move= "r" 
        print("rock")
    if computer_move==2:  #elif can be used here as it will only check if first if not true
        computer_move='p'
        print("paper")
    if computer_move==3:   #elif can be used  
        computer_move='s'
        print("scissor")
    if player_move==computer_move:
        print("tied")
        tied=tied +1
    elif player_move=='r'and  computer_move=='p':
        print("you lost")
        loss= loss+1
    elif player_move=='p' and computer_move=='s':
        print("you lost")
        loss= loss +1
    elif player_move=='s'and computer_move=='r':
        print("you lost")
        loss=loss+1
    elif player_move=='r'and computer_move=='s':
        print("you won")
        wins=wins+1
    elif player_move=='p'and computer_move=='r':
        print("you won")
        wins=wins+1
    elif player_move=='s'and computer_move=='p':
        print("you won")
        wins=wins+1