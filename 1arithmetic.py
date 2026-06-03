#develop a python program to read 2 numbers from the keyboard and perform basic arithmatic opration based on the choice
num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
print("\nMenu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division ")
ch = int(input("Enter your choice: "))
if ch ==1:
    print(num1+num2)
elif ch ==2:
    print(num1-num2)
elif ch == 3: 
    print(num1*num2)
elif ch ==4:
    if num2!=0:
        print(num1/num2)
    else:
        print("ZeroDivisionError")
else:
    print("Invalid choice give a proper choice")