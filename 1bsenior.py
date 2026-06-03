#Devlop a python program read a name and year of 4 common person display whether the person is a senior citizen or not
name = input("Enter the name: ")
year = 2026
dob = int(input("Enter the year of birth: "))
age = year-dob
if age >60:
    print(name," is a senior citizen")
else:
    print(name,"is not a senior citizen")