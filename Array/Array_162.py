a,b=map(int,input(":").split(" "))
listin=[int(n) for n in input().split(" ",a-1)]
num=-1

if listin.__contains__(b):
    num = b
else:
    for i in range(b,0,-1):
        if listin.__contains__(i):
            num = i
            break
print(num)
