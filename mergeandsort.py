'''Program to 
    1.define two lists 
    2.take integer values from the user
    3.Display the lists
    4.merge the lists
    5.sort the merged list and display'''

n1=int(input("Enter the size of list 1: "))
n2=int(input("Enter the size of list 2: "))

lst1=[]
lst2=[]

for i in range(n1):
    lst1.append(int(input("Enter integer element to lst1: ")))

for i in range(n2):
    lst2.append(int(input("Enter integer element to lst2: ")))

print("The lists are :",lst1,lst2,sep='\n')
lst3=lst1+lst2

print("After merging the two lists as single list",lst3)

lst3.sort()

print("After sorting the elements of merged list :",lst3)