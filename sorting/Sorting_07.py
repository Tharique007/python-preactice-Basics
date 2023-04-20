a=int(input(":"))
list1=[]
for i in str(a):
    list1.append(int(i))
list1.sort()
print(list1)
outt=0
b=len(list1)
count=0
for j in list1:
    chill = 1
    if j>0:
        for i in range(1,b):
            chill *= 10
        b = b -(1+count)
        count = 0
    elif j == 0:
        count +=1
    outt = outt+(j*chill)
print(outt)