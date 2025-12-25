'''Program to
    1.Define an empty list with user defined size
    2.initialize a variable to 0 (will be used to hold the sum)
    3.Prompt the user to enter integer elements
    4.Add the elements of the list parallely and store sum in the 0 initialised variable.'''
n=int(input("Enter the size of list:"))

l=[]
s=0

for i in range(n):
    l.append(int(input("Enter an integer :")))
    s+=l[i]
    
print("The list is :",l)
print("Sum of elements in the list is:",s)
    
