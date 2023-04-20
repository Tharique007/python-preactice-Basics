a,b=map(int,input(":").split(" "))
difference= abs(a-b)

if difference%2==0:
    print("even")
else:
    print("odd")