'''Program to 
    1.open a file in append mode.
    2.define an empty list
    3.generate 20 random numbers between 1-100 and append them in the list
    4.Add that list to the opened file.'''

import random

f=open("src.txt",'a+')
l=[]

for i in range(20):
    l.append(str(random.randint(1,100)),'\n')

f.writelines(l)

f.seek(0)
print(f.read())
