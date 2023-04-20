a=int(input(":"))
listin=[]
listout=[]
for i in range(a):
    listproc=[x for x in input().split(" ",4-1)]
    listproc[1] = int(listproc[1])
    listproc[2] = int(listproc[2])
    listproc[3] = int(listproc[3])
    listin.append(listproc)
list_math=[]

for i in listin:
    if i[3] not in list_math:
        list_math.append(i[3])
list_math.sort(reverse=True)
#print(list_math)

for j in list_math:
    list_cs=[]
    list_cs1=[]
    cs_count=0
    for k in listin:
        if k[3] == j:
            if k[2] not in list_cs:
                list_cs.append(k[2])
            list_cs1.append(k)
            cs_count +=1
    list_cs.sort(reverse=True)
    #print("list_cs",list_cs)
    #print("list_cs1", list_cs1)
    #print("cs_count", cs_count)
    if cs_count > 1:
        for j1 in list_cs:
            list_en=[]
            list_en1=[]
            en_count=0
            for k1 in list_cs1:
                if k1[2] == j1:
                    if k1[1] not in list_en:
                        list_en.append(k1[1])
                    list_en1.append(k1)
                    en_count += 1
            list_en.sort(reverse=True)
            #print("list_en",list_en)
            #print("list_en1", list_en1)
            #print("en_count",en_count)
            if en_count > 1:
                for j2 in list_en:
                    for k2 in list_en1:
                        #print("k2:", k2)
                        if k2[1] == j2:
                            listout.append(k2)
                    #print("listout_en",listout)
            else:
                listout.append(list_en1[0])
    else:
        listout.append(list_cs1[0])
#print(listout)
for d in listout:
    print(*d)


