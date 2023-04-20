a=int(input(":"))
listvalues=[0]*a
for i in range(a):
    lista=[]
    a=int(input())
    lista.append(a)
    lis1=[int(n) for n in input().split(" ",a-1)]
    lista.append(lis1)
    lis2=[int(n) for n in input().split(" ",(a-1)-1)]
    lista.append(lis2)
    listvalues[i] =lista
print(listvalues)
output=[]

for index in listvalues:
    for i in range(index[0]):
        if i<((index[0])-1):
            if index[1][i] != index[2][i]:
                output.append(i)
                break
        elif i == ((index[0])-1):
            output.append(i)
print(*output)