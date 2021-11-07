input_string = input("Enter a list element separated by space ")
list  = input_string.split()
print("Calculating sum of element of input list")
def Sum(num):
    sum = 0
    for num in list:
        sum += int (num)
    return sum
Result = Sum(list)
print("Sum = ",Result)