'''Program to
    1.Take a string as input from the user
    2.Take an integer as shift value from the user
    3.Transfer x characters where x equals shift value from beginning to the end of the same string '''

st=input("Enter a string :")
sh=int(input("Enter shift value :"))

nst=""

nst+=st[sh:]
nst+=st[:sh]

print(nst)