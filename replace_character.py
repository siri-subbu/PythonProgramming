'''Program to
    1.take a string as input from the user.
    2.replace a letter in the string with another
    3.The program just has the case of replaceing a with x in user defined string.'''

st=input("Enter a string :")
nst=""

for letter in st:
    if letter=='a':
        nst+='x'
    else:
        nst+=letter

print(f"After replacement the string is {nst}")