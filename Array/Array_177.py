a,b=map(int,input(":").split(" "))
listin=[int(n) for n in input(" ").split(" ",a-1)]
listin.sort(reverse=True)
print(listin[b-1])