string1,string2=input(":").split(" ")
lis1=[]
lis2=[]
for k in string1:
    if k not in lis1:
        lis1.append(k)
for l in string2:
    if l not in lis2:
        lis2.append(l)
list11=[]
list22=[]
#print(lis1 , lis2)
result = True

if len(string1) == len(string2) and len(lis1) == len(lis2):
    for i in lis1:
        listx=[]
        for j in range(0,len(string1)):
            if i == string1[j]:
                listx.append(j)
        list11.append(listx)
    #print(list11)
    for i in lis2:
        listy=[]
        for j in range(0,len(string2)):
            if i == string2[j]:
                listy.append(j)
        list22.append(listy)
    #print(list22)
    for ln in range(0,len(list11)):
        #print("ln:",ln)
        if len(list11[ln]) == len(list22[ln]):
            for ind in range(0,len(list11[ln])):
                #print("ind:",ind)
                if list11[ln][ind] == list22[ln][ind]:
                    continue
                else:
                    result
                    print(-1)
                    break
        else:
            result = False
            print(-1)
            break
else:
    result = False
    print(-1)
if result == True:
    print("yes")