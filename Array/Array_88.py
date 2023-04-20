a,b=map(int,input().split(" "))
list1=[]
for i in range(0,a):
    list1.append(input())
print(list1)
res=0
for i in range(0,(a-b+1)):
    cont = 0
    for j in range(i,(i+b-1)):
        if list1[j] == list1[i+1]:
            cont += 1
            res = cont
            #print("cont:", cont)
        else:
            break
#print(res)
if res < b-1:
    print("no")
else:
    print("yes")