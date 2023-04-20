a,b=map(int,input().split(" "))
list1=[int(B) for B in input().split(" ",a-1)]

def k_minelement(K,lista):
    listb = []
    for i in lista:
        if i not in listb:
            listb.append(i)
    listb.sort()
    length = len(listb)
    if K<length:
        return listb[0+K-1]
    else:
        return -1
print(k_minelement(b,list1))
