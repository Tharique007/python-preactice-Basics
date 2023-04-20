a,b =map(int,input().split(" "))
list1=[int(num) for num in input().split(" ",a-1)]
list2=[" "]*a

for i in range(0,a):
    if (i+b) < a:
        list2[i+b] = list1[i]
    elif (i+b)>=a:
        try:
            list2[(i+b)-a] = list1[i]
        except:
            if a<b and i==(a-1):
                list2[(i + b) - (a*2)] = list1[i]

print(*list2)