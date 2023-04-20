N,K = map(int,input().split())
listN=[int(n) for n in input().lstrip().split(" ",N-1)]
output=[]
for i in listN:
    if i<K:
        output.append(i)
if len(output) >0:
    output.sort()
    print(*output)
else:
    print("-1")