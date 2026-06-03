'''Develop a program to print 10 most frequently appearing words in a text file. [Hint: Use
a dictionary with distinct words and their frequency of occurrences. Sort the dictionary in
the reverse order of frequency and display the dictionary slice of the first 10 items.'''
import sys
import string
import os.path
fname = input("Enter the file name: ")
if not os.path.isfile(fname):
    print("The file doesn't exists")
    sys.exit(0)
fopen = open(fname,"r")
wordFreq = {}
filecontent = ''

for word in fopen:
    for ch in word:
        if ch not in string.punctuation:
            filecontent+=ch
        else:
            filecontent+=""

words = filecontent.split()
for wor in words:
    if wor in wordFreq:
        wordFreq[wor]+=1
    else:
        wordFreq[wor]=1
print(wordFreq)
wordsort = sorted(wordFreq.items(), key = lambda item : item[1], reverse=True)
print("the top 10 most frequently repeating words are ")
for word, freq in wordsort[:10]:
    print(word,"occurs",freq,"times")
