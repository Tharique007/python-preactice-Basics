a=int(input(":"))
listin=[]
for i in range(a):
    for i in [int(n) for n in input().split(" ")]:
        if i not in listin:
            listin.append(i)
listin.sort()
print(*listin)