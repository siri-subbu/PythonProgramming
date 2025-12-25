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
