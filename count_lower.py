'''Program to
    1.take a string as input from the user
    2.Count the number of lower case alphabets in entire string 
    without built-in methods and display'''

st=input("Enter a string :")
c=0

for letter in st:
    if ord(letter)>=97 and ord(letter)<=122:
        c+=1

print(f"The count of lower letters is {c}")