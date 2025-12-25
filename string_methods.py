'''Program to demonstrate methods of strings'''

st="MVGR College of Engineering"

print(st.capitalize())#'Mvgr college of engineering'

print(st.casefold())#'mvgr college of engineering'

print(st.center(50))#'           MVGR College of Engineering            '
print(st.center(50,'*'))#'***********MVGR College of Engineering************'
print(st.ljust(50,'$'))#MVGR College of Engineering$$$$$$$$$$$$$$$$$$$$$$$
print(st.rjust(50,'#'))# #######################MVGR College of Engineering

print(st.count('eg'))#1
print(st.count('e'))#4
print(st.count('e',13))#2
print(st.count('e',0,12))#2

print(st.endswith('ing'))#True
#print(st.endswith('ege',,11))#SyntaxError: invalid syntax
print(st.endswith('ege',0,11))#False
print(st.endswith('ege',0,12))#True
print(st[12])#' '
print(st[11])#'e'
print(st.endswith(('on','hello','ing')))#True
print(st.endswith(('on','hello','in')))#False
print(st.startswith('MV'))#True

print("MVGR\tCollege\tof\tEngineering".expandtabs())#'MVGR    College of      Engineering'
print("MVGR\tCollege\tof\tEngineering".expandtabs(15))#'MVGR           College        of             Engineering'

print(st.find('g'))#10
print(st.find('G'))#2
print(st.rfind('g'))#26
print(st.rfind('G'))#2
print(st.find('G',11))#-1
print(st.find('g',11))#18
print(st.find('g',8,27))#10
print(st.rfind('G',11))#-1
print(st.rfind('g',11))#26
print(st.rfind('g',8,27))#26

print('My name is {0} and I\'m {1} years old.'.format('Nayani',14))#My name is Nayani and I'm 14 years old.

str="This is a {} program"
print(str.format("python"))#This is a python program.

a={'x':'Jahnavi','y':'Siri','z':'Priya'}
print("Hello {x}, This is {y} and meet my benchmate {z}.".format(**a))#Hello Jahnavi, This is Siri and meet my benchmate Priya.
print("Hello {x}, This is {y} and meet my benchmate {z}.".format_map(a))#Hello Jahnavi, This is Siri and meet my benchmate Priya.

profession={'name':['Aswani','Lasya','Mounika'],'Department':['CSE','EEE'],'profession':['faculty member','student']}
print('{name[0]} is a {profession[0]} in the department of {Department[0]},{name[1]} is a {profession[1]} in the department of {Department[0]},{name[2]} is a {profession[1]} in the department of {Department[1]}'.format_map(profession))
#Aswani is a faculty mamber in the department of CSE,Lasya is a student in the department of CSE,Mounika is a student in the department of EEE

s={'Hello','world'}
print('*'.join(s))#'Hello*world'

print('Hello*world'.split('*'),st.split(' '),sep='\n')
#['Hello', 'world']
#['MVGR', 'College', 'of', 'Engineering']

print(st.title())#Mvgr College Of Engineering

print(st.upper())#MVGR COLLEGE OF ENGINEERING

print(st.lower())#mvgr college of engineering

print(st.isalnum())#False
print("MVGR123".isalnum())#True
print('581'.isdigit())#True
print(" ".isspace())#True
print("MVGR ".isspace())#False
print("MVGR@123".isprintable())#True
print(" ".isprintable())#True
print("MVGR ".isspace())#False
