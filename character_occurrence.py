'''Program to count the number of occurrences of a character in a string without built in methods.'''

st=input("Enter a sring :")
c=input("Enter a character to get its count :")

count=0

for letter in st:
    if letter==c:
        count+=1

print("The count of",c,"in",st,"is",count)