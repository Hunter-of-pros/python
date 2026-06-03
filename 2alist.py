'''Write a python program to create a list and perform the following operations
• Inserting an element
• Removing an element
• Appending an element
• Displaying the length of the list
• Popping an element
• Clearing the list'''
lst = []
lst.insert(0,1)
lst.insert(1,2)
lst.insert(2,3)
print("The list after insertion is ",lst)
lst.remove(3)
print("The list after removal is ",lst)
lst.append(4)
print("The list after addending is", lst)
print("The length of the list is", len(lst))
po = lst.pop()
print("The list after popping",po,"is",lst)
print("The list after clearing is ", lst.clear())
