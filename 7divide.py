import sys
def divExp(a,b):
    assert a>0 ,"a should be greater than 0"
    try:
        c=a/b
    except ZeroDivisionError:
        print("Value of b cannot be zero")
        sys.exit(0)
    else:
        return c
    
num1 = int(input("Enter the value of a"))
num2 = int(input("Enter the value of b"))
num3 = divExp(num1,num2)
print(num1,"/",num2,"=",num3)
