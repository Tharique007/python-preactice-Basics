a=int(input(":"))
facorts=[]
oddfact=[]
for i in range(1,a+1):
    if a%i==0 and i not in facorts:
        facorts.append(i)
for j in facorts:
    if j%2!=0:
        oddfact.append(j)
print(*oddfact)


