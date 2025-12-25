'''Program to
    1.Open a file in read mode
    2.And demonstrate the functionality of methods (seek,tell,flush)'''

f=open("src.txt","r")

print(f.read())

print(f"The position of the file pointer is {f.tell()}")

f.seek(4)
print(f.readline())

print(f"The position is {f.tell()}")

f.flush()

print(f.read())