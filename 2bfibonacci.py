#fibonacci sequence 0 1 1 2 3

n = int(input("How long should the sequence be:"))
num1 = 0
num2 = 1
print(num1, num2, end = " ")
for i in range (2,n):
    currterm = num1 + num2
    print(currterm, end =" ")
    num1 = num2
    num2 = currterm
print()
