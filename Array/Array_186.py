a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
count=0
for i in range(0,len(listin)):
    num = abs(listin[i]*(i+1))
    if listin.__contains__(num):
        count += 1
print(count)