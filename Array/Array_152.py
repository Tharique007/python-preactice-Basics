a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listenout=[]
b=len(listin)
for i in range(0,b):
    sum_of_sufix=0
    for j in range(i,b):
        #print("j:", j)
        sum_of_sufix += listin[j]
    sum_of_prefix=0
    for k in range(i,-1,-1):
        #print("k:", k)
        sum_of_prefix += listin[k]
    sum=sum_of_sufix + sum_of_prefix
    listenout.append(sum)
print(*listenout)