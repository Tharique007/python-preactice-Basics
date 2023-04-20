a,b,c=map(int,input(":").split(" "))
listin=[int(n) for n in input().split(" ",a-1)]
print(min(listin[b-1:c+1]))