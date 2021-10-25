Player1 = str(input("Player 1 chooses: ")).lower()
Player2 = str(input("player 2 chooses: ")).lower()
if (Player1 == Player2):
    print("its a tie")
elif (Player1 == 'rock'):
    if (Player2=='scissor'):
        print("Player1 is the winner")
    elif(Player2=='paper'):
        print("Player 2 is the winner")
elif (Player1 == ' scissor'):
    if(Player2=='rock'):
        print("Player2 is the winner")
    elif(Player2=='paper'):
        print("Player1 is the winner")
elif(Player1=='paper'):
    if(Player2=='scissor'):
        print("Player2 is the winner")
    elif(Player2=='rock'):
        print("Player1 is the winner")
else:
    print("Invalid input!")

