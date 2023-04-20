a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
listpro=listin.copy()
listpro.sort()
count=0

for i in range(0,len(listin)):
    if listpro[i] != listin[i]:
        num1 = listin[i]
        num2 = listpro[i]
        in1= i
        in2=listin.index(num2)
        listin[in1] = num2
        listin[in2] = num1
        count += 1
print(count)