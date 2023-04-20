x=int(input(":"))
list1=[int(n) for n in input().split(" ",x-1)]
list2=[int(k) for k in input().split(" ",x-1)]


def mirrorarray(a,lista,listb):
    result = True
    for i in range(a):
        if lista[i] == listb[a-1-i]:
            result = True
        else:
            result = False
            print("no")
            break
    return result

if mirrorarray(x,list1,list2) == True:
    print("yes")

