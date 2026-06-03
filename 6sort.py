'''Develop a program to sort the contents of a text file and write the sorted contents into a
separate text file. [Hint: Use string methods strip(), len(), list methods sort(), append(), and
file methods open(), readlines(), and write()]'''
import sys
import os.path
fname = input("Enter the file name: ")
if not os.path.isfile(fname):
    print("The file does not exists")
    sys.exit(0)
fopen = open(fname,'r')
lines = fopen.readlines()
print (lines)
linelst = []
for line in lines:
    linelst.append(line.strip())
linelst.sort()
fwrite = open("sort.txt","w")
for line in linelst:
    fwrite.write(line+"\n")
fopen.close()
fwrite.close()
file = open("sort.txt","r")
content = file.readlines()
for i in content:
    print(i,end = "")