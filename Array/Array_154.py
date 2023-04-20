a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
result = False
for i in range(0,len(listin)):
    sumOfsufix=0
    for j in range(i,len(listin)):
        sumOfsufix += listin[j]
    sumOfPerfix=0
    for k in range(i,-1,-1):
        sumOfPerfix += listin[k]
    if sumOfPerfix == sumOfsufix:
        #print(i)
        result = True
        break
if result:
    print("yes")
else:
    print("no")
