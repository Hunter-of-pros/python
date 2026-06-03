#mean variance standard deviation
from math import sqrt
lst =[]
n = int(input("Enter how many numbers you want to enter: "))
for i in range(n):
    num = int(input("Enter a number: "))
    lst.append(num)
total=0
for i in lst:
    total +=i
mean = total /n
total = 0
for i in lst:
    total = (mean-i)**2
variance = total/n
stddeviation = sqrt(variance)
print("Mean is : %.2f"% mean)
print("variance is : %.2f"% variance)
print("Standard Deviation is : %.2f"%stddeviation)
