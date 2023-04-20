a=int(input(":"))
listin=[int(n) for n in input().split(" ")]
count=0
for i in range(0,len(listin)):
    for j in range(0,len(listin)):
        if i<j:
            count += 1
print(count)