a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
rotation=0
listexpected=list1.copy()
listexpected.sort()
result = False
while(result == False):
    for i in range(0,a):
        if listexpected[i]==list1[i]:
            continue
        else:
            inde = list1.index(listexpected[i])
            if inde < (a-1):
                diff = abs(inde - i)
                rotation += 1
                round=0
                for i in range(i,(i+diff)):
                    l=list1[i]
                    list1[i]=list1[inde+round]
                    list1[inde+round]=l
                    round +=1
    if list1 == listexpected:
        result = True
    else:
        result = False
if rotation > 0:
    print(rotation)
else:
    print(-1)