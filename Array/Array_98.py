a=int(input(":"))
list1=[int(c) for c in input().split(" ",a-1)]

def SumOfAllConsecutivePair(lista):
    sum=0
    for i in range(1,len(lista)):
        d=lista[i]+lista[i-1]
        sum += d
    return sum
print(SumOfAllConsecutivePair(list1))