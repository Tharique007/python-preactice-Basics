a=int(input(":"))
lisin=[]
for i in range(a):
    lisin.append(input())
vowellist=["a","e","i","o","u"]
outputdic=dict()
for i in lisin:
    vowelcount=0
    for j in i:
        if j.lower() in vowellist:
            vowelcount += 1
    outputdic[i]=vowelcount
print(outputdic)
listval= list(outputdic.values())
listval.sort(reverse=True)
print(listval)
outputlist=[]
for i in listval:
    for j,k in outputdic.items():
        if k == i and j not in outputlist:
            outputlist.append(j)
            print(j)
#print(*outputlist)
