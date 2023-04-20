a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listout=[]
sum = 0
for i in listin:
    sum += i
    listout.append(sum)
print(*listout)