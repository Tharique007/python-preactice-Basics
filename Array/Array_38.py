a,b=map(int,input().split(" "))
list_in=[0]*a
ooutput=[]

for i in range(a):
    list_in[i]=[int(num) for num in input().split(" ",b-1)]

for i in list_in:
    for j in i:
        if j not in ooutput:
            ooutput.append(j)
ooutput.sort()
for i in range(0,len(ooutput),3):
    output1 = ""
    for j in range(i,i+b):
        output1 = output1+ str(ooutput[j])+" "
    print(output1.rstrip())
