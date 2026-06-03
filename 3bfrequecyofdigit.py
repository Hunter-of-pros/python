#frequency of digits from char
num = input("Enter the digits")
print("The digits entered is", num)
uniqdig = set(num)
print(uniqdig)
for i in uniqdig:
    print(i,"occurs",num.count(i))