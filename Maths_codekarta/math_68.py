P,A=map(int,input(":").split(" "))
halfp=int(P/2)
result = False
for i in range(1,halfp+1):
    j=halfp-i
    if i*j == A:
        result = True
if result:
    print("yes")
else:
    print("no")