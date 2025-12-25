'''Program to
    1.Take a word as input from the user.
    2.store the reverse of that word in another variable
    3.check for each character in both strings for equality
    4.Finally print whether the given string is palindrome or not'''

st=input("Enter a word :")
rst=st[::-1]

for i in range(len(st)):
    if st[i]==rst[i]:
        pass
    else:
        if abs(ord(st[i])-ord(rst[i]))==32:
            pass
        else:
            break

if (i+1)==len(st):
    print(st,"is a palindrome")
else:
    print("Its not a palindrome")