a=int(input(":"))
L1=[int(n) for n in input().split(" ",a-1)]
L2=[int(m) for m in input().split(" ",a-1)]
L3=[]
output=""
for i in L1:
    if i not in L3 and i in L2:
        L3.append(i)
        output += str(i)
if len(output) > 0:
    print(" ".join(output))
else:
    print(-1)

