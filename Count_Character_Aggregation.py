'''Program to
    1.Take a string a input from the user and store in a variable.
    2.store the length of user entered string to a variable.
    3.define an empty dictionary.
    4.The key will be the count starting from 1.
    5.Value will be a unique list that contains the characters of the string whose appearance equal to key.'''
s=input("Enter a string: ")
n=len(s)
d={}
for i in range(n):
    d[i]=[]
    for j in s:
        if s.count(j)==i:
            if j not in d[i]:
                d[i].append(j)
    if len(d[i])==0:
        del d[i]
print(d)
