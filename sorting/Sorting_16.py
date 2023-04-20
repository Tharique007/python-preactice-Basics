a=int(input())
lista=[int(A) for A in input().split(" ",a-1)]
b=int(input())
listb=[int(B) for B in input().split(" ",b-1)]

listc=lista+listb
listd=[]
for i in listc:
    if i not in listd:
        listd.append(i)
listd.sort()
print(*listd)