Element1 = list(input("enter list of accounts for Element1 :").split(","))
Element2 = list(input("enter list of accounts for Element2 :").split(","))
a=[]
for i in Element1:
    if (int(i)%2!=0):
        a.append(i)
print(a)
for i in Element2:
    if(int(i)%2==0):
        a.append(i)
print(a)