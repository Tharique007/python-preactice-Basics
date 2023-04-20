a=int(input(":"))
b=str(a)
length=len(b)
sum=0
for i in b:
    sum += int(i)**length
print(sum)