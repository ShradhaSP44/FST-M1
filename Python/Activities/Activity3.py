Player1 = input("what is the name of 1st Player: ").upper()
Player2= input("what is the name of 2nd player: ").upper()
Player1_Choice = str(input("Player 1 chooses: ")).lower()
Player2_Choice = str(input("player 2 chooses: ")).lower()
if (Player1_Choice == Player2_Choice):
    print("its a tie")
elif (Player1_Choice == 'rock'):
    if (Player2_Choice=='scissor'):
        print("the winner is",Player1)
    elif(Player2_Choice=='paper'):
        print("the winner is",Player2)
elif (Player1_Choice == ' scissor'):
    if(Player2_Choice=='rock'):
        print("the winner is",Player2)
    elif(Player2_Choice=='paper'):
        print("the winner is",Player1)
elif(Player1_Choice=='paper'):
    if(Player2_Choice=='scissor'):
        print("the winner is",Player2)
    elif(Player2_Choice=='rock'):
        print("the winner is",Player1)
else:
    print("Invalid input!")

