n,k=map(int,input(":").split(" "))
value=1
for i in range(((n-k)+1),n+1):
    #print(i)
    value *= i
print(value)