def Sum(num):
  if num:
    return num + Sum(num-1)
  else:
    return 0
res = Sum(int(input("enter the no: ")))
print(res)