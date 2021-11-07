Fruit ={"apple": 10,"orange": 50, "banana": 20,"mango":15}
Fruit_Check = str(input("What fruit do you want: ")).lower()
if(Fruit_Check in Fruit):
    print(Fruit_Check+" - Fruit is present")
else:
    print(Fruit_Check+" - Fruit is not present")
    