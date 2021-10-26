Player1 = input("Enter the Player1's name: ").upper()
Player2 = input("enter the Player2' name: ").upper()
while True:
    Player1_Choice = str(input(Player1+" chooses: ")).lower()
    Player2_Choice = str(input(Player2+" chooses: ")).lower()
    if (Player1_Choice==Player2_Choice):
        print("its a tie")
    elif(Player1_Choice=='rock'):
        if(Player2_Choice=='paper'):
            print(Player2+" is the winner")
        elif(Player2_Choice=='scissor'):
            print(Player1+" is the winner")
    elif(Player1_Choice=='paper'):
        if(Player2_Choice=='rock'):
            print(Player1+" is the winner")
        elif(Player1_Choice=='scissor'):
            print(Player2+" is the winner")
    elif(Player1_Choice=='scissor'):
        if(Player2_Choice=='paper'):
           print(Player1+" is the winner")
        elif(Player2=='rock'):
            print(Player2+" is the winner")
    else:
       print("invalid input")
    Player1_ask = str(input (Player1+", Do you want to play? ")).lower()
    Player2_ask= str(input (Player2+", Do you want to play? ")).lower()
    if (Player1_ask=='yes'):
        if (Player2_ask=='yes'):
            pass
        else:
            print("End of game")
            raise SystemExit
    elif(Player1_ask=='no'):
        print("End of game")
        raise SystemExit
    else:
        print("invalid input")
        raise SystemExit