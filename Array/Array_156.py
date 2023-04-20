a=int(input(":"))
b=len(str(a))
sum=0
for i in range(b-1,-1,-1):
    #print(i)
    sum += (a%10)**i
    a=int(a/10)
print(sum)
