listin=input(" ").split(" ")
listin[2] = int(listin[2])
a=len(listin[0])
b=len(listin[1])
if a == b:
    count = 0
else:
    count = abs(a-b)
    if a>b:
        c=listin[0]
        listin[0]=listin[1]
        listin[1]=c
for i in range(0,len(listin[0])):
    if listin[0][i] != listin[1][i]:
        count +=1
if count == listin[2]:
    print("yes")
else:
    print("no")

