a,b = map(int,input(":").split(" "))
count=0
from math import sqrt
for i in range(a,(b+1)):
    j = sqrt(i)
    #print("j:",j)
    if j in range(1,(b+1)):
        #print(i)
        count +=1
    #print("count: ", count)
#print(count)
if count>0:
    print(count)
else:
    print(-1)
