a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listin.sort()
result = True
for i in range(0,len(listin)):
    #print(i,listin[i],(i+1))
    if listin[i] != (i+1):
        result=False
        break
if result:
    print("yes")
else:
    print("no")