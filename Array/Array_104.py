a,b=map(int,input(":").split(" "))
listall=[int(A) for A in input().split(" ",(a+b)-1)]
lista=[x for x in listall[0:a]]
listb=[x for x in listall[a:(a+b)]]
listout=[Y for Y in lista if Y in listb]
listout.sort()
print(*listout)
