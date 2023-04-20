a,b=map(int,input().split(" "))
listin=[int(n) for n in input().split(" ",a-1)]
output = "no"
for i in range(0,len(listin)):
    for j in range(i+1,len(listin)):
        if listin[i]+listin[j] == b:
            output = "yes"
            break
print(output)