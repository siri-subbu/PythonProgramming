'''Program to 
    1.Define an empty list
    2.Prompt the user to enter the size of the list
    3.Prompt the user to enter the integer elements to the defined list
    4.Display the list
    5.Define another empty list
    6.Add the elements from the first list to the new list by removing duplicate elements
    7.Display the list from which duplicates are removed'''
n=int(input("Enter the size of the list: "))
lst=[]
for i in range(n):
    lst.append(int(input("Enter integer :")))
ul=[]
print("The list is : ",lst)
for i in lst:
    if i not in ul:
        ul.append(i)    
print("List after removing duplicates elements ",ul)
