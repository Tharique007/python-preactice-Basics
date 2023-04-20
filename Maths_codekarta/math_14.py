inputin=input(":")
max=0
count=0
for i in inputin:
    if int(i) == 1:
        count+=1
        #print("if",count)
    elif int(i) == 0:
        if count>max:
            max = count
        count=0
if count > max:
    max = count
if max>0:
    print(max)
else:
    print(-1)


