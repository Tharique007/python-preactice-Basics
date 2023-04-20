a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listin.sort()
lenthofsub = 0
#print(listin)

for i in range(0,a):
    count=0
    num=0
    for j in range(i,a):
        if listin[i]+num == listin[j]:
            count += 1
        else:
            break
        num += 1
    if count > lenthofsub:
        lenthofsub = count

print(lenthofsub)