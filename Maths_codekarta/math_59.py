inputstr=input(":")
listin=[]
count=0
for i in inputstr:
    if i not in listin:
        listin.append(i)
        if inputstr.count(i) ==1:
            count += 1
if count > 0:
    print(count)
elif count == 0:
    print(-1)