a=int(input(":"))
listyear=[int(num) for num in input().split(" ",a-1)]
listparty= [party for party in input().split(" ",a-1)]
for j in range(0,a):
    for i in range(j,a):
        if listyear[i]<listyear[j]:
            k = listyear[i]
            listyear[i] = listyear[j]
            listyear[j]=k
            l=listparty[i]
            listparty[i]=listparty[j]
            listparty[j]=l
#print(listyear)
#print(listparty)
count=0
index=a
for i in range(0,a-1):
    if listparty[i] != listparty[i+1]:
        count=0
        index=i
        print(listyear[i+1])
    elif listparty[i] == listparty[i+1]:
        count = count+1

