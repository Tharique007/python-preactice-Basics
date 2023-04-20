a=int(input(":"))
listas = [int(s) for s in input().split(" ",a-1)]
def sorting(listin):
    maximum=max(listin)
    count=[0]*(maximum+1)
    for i in range(0,(maximum+1)):
        if listin.count(i) > 0:
            count[i] = listin.count(i)
    #print("1",count)
    summ=count[0]
    for j in range(1,(maximum+1)):
        if count[j] > 0:
            count[j] = count[j]+summ
            summ=count[j]
    #print("2",count)
    listprocess=[]
    for d in listin:
        if d not in listprocess:
            listprocess.append(d)
    outputlist=[0]*max(count)
    #print(outputlist)
    listprocess.sort(reverse=True)
    #print(listprocess)
    for e in listprocess:
        don = count[e]-1
        #print(don)
        for i in range(don,-1,-1):
            outputlist[i]=e
    return outputlist



print(*sorting(listas))