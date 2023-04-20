a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listproc=[]
for i in listin:
    if i not in listproc:
        listproc.append(i)
for i in listproc:
    if listin.count(i) == 1:
        print(i)