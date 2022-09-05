def add_(a,b):
    return a+b
def sub_(a,b):
    return a-b
def mul_(a,b):
    return float(a)*float(b)
def div_(a,b):
    return float(a)/float(b)
print("Simple Calculator\n")
num2 = None
while (num2 == None):
    try:
        num1, op, num2 = map(str,input("Enter equation : ").split())
    except ValueError:
        print("There must be space between your characters.")
num1 = int(num1)
num2 = int(num2)
if (op == "+"):
    print (f"Sum of {num1} and {num2} = {add_(num1,num2)}")
elif (op == "-"):
    print (f"Difference of {num1} and {num2} = {sub_(num1,num2)}")
elif (op == "*"):
    print (f"Product of {num1} and {num2} = {mul_(num1,num2)}")
elif (op == "/"):
    print (f"Dividing {num1} by {num2} = {div_(num1,num2)}")
else :
    print("It solves only basic equations containing following operations : +,-,*,/")
