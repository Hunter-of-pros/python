'''Develop a program to read 6 subject marks from the keyboard for a student. Generate a
report that displays the marks from the highest to the lowest score attained by the student.
[Read the marks into a 1-Dimesional array and sort using the Bubble Sort technique].'''
marks = []
for i in range(6):
    m = int(input("Enter the marks of subject"))
    marks.append(m)
for i in range(6):
    for j in range(5):
        if marks[j]<marks[j+1]:
            marks[j],marks[j+1]=marks[j+1],marks[j]
print("marks from highest to lowest: ")
print(marks)