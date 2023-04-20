a,b=map(int,input().split(" "))
listin=[int(n) for n in input().split(" ",a-1)]
result=False

for i in range(0,len(listin)-1):
    for j in range(i+1,len(listin)):
        if listin[i]+listin[j] == b:
            print(listin[i],listin[j])
            result = True
            break
    if result == True:
        break
if result:
    print("yes")
else:
    print("no")