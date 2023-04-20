a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]

def leastoccurance(lista):
    min=len(lista)
    output=0
    listb=[]
    for i in lista:
        if i not in listb:
            listb.append(i)
    for i in listb:
        if lista.count(i) < min:
            min = lista.count(i)
            output = i
    return output
print(leastoccurance(list1))