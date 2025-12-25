'''Program to
    1.import os module
    2.print current working directory
    3.open a file x+ mode(create along with read and write)
    4.Write a string into the file
    5.showing the functionality of methods of files in python'''

import os

print(os.getcwd())

f=open("src.txt","x+")

f.write("Hello! This is the first file\n")

print("Now you'll see the first 5 characters of the file\n")
f.seek(0)
print(f.read(5))

print("Now it's turn to watch a whole line(single)\n")
print(f.readline())

I=["\nThis is line 2\n","This is line 3\n"]
f.writelines(I)
f.seek(0)

print("You'll find all the lines as elements of a list\n")
print(f.readlines())

d=f.close()

if not d:
    print("File got closed")
