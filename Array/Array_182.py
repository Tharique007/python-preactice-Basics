a,b=map(int,input(":").split(" "))
listin=[int(n) for n in input().split(" ",a-1)]

num = -1
if listin.__contains__(b):
    num = listin.index(b)
else:
    result = False
    num1= b-1
    while(result == False and num1 >= 0):
        if listin.__contains__(num1):
            num = listin.index(num1)
            result = True
            break
        num1 -= 1
print(num)