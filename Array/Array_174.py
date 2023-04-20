a=int(input(":"))
listin=[int(n) for n in input(":").split(" ",a-1)]
maximum=0

for i in range(0,len(listin)-1):
    sum=0
    for j in range(i,len(listin)):
        sum += listin[j]
    if sum > maximum:
        maximum = sum
print(maximum)