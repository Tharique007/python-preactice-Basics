a1,b1,c1 = input("enter the sides to be checked").split()
a=int(a1)
b=int(b1)
c=int(c1)
if a != b and b !=c and b != a:
    if a+b>c and b+c>a and c+a>b:
        print("yes")
    else:
        print("no")
else:
    print("no")