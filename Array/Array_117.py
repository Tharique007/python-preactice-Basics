a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
count1=0
summation1=0
for k in range(0,a-1):
    sum1=listin[k]
    coun1=1
    for i in range(k,a-1):
        if listin[i+1]>listin[i]:
            sum1 += listin[i+1]
            coun1 += 1
        else:
            break
    #print(count1, summation1)
    if sum1>summation1:
        summation1 = sum1
    if coun1 > count1:
        count1 = coun1
print(summation1)



