a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
count = 0
listop=[]
for i in range(0,a):
    for j in range(0,a):
        deling = ""
        if i < j and listin[i] < listin[j]:
            deling = str(listin[i])+str(listin[j])
            if int(deling) not in listop:
                listop.append(int(deling))
                count += 1
if count >0:
    print(count)
else:
    print(-1)
