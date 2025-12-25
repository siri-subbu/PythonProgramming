st=input("Enter a string :")
sh=int(input("Enter shift value :"))
nst=""
nst+=st[sh:]
nst+=st[:sh]
print(nst)