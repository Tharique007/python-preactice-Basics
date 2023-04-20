a,b=map(int,input(":").split(" "))
min=min(a,b)
for i in range(min,0,-1):
    if a%i==0 and b%i==0:
        print(i)
        break