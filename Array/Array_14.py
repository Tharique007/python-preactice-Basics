n,w=map(int,input().split(" ",2-1))
listin=[int(num) for num in input().split(" ",n-1)]
output=""
for i in range(0,len(listin)-1):
    output1=""
    for j in range(i,(i+w)):
        if listin[j] == 0:
            output1 = output1 + str(j+1)+" "
            break
    if len(output1)>0:
        output = output+output1
    elif len(output1)==0:
        output = output + "-1"+" "
print(output.rstrip())


