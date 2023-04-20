A,B= [int(A)for A in input().split()]
C= str(input())
D=C.split(" ")
E=[]
print(D)

for i in D:
    if int(i)!=B:
        E.append(int(i))
if len(E) !=0:
    for j in E:
        print(j,end=" ")
else:
    print("empty")