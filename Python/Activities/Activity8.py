User_Enter = list(input("Enter the list of numbers: ").split(","))
First= User_Enter[0]
Last=User_Enter[-1]
if (First==Last):
    print("True")
else:
    print("False")