a,b = map(int,input(":").split(" "))
count=0
a=str(a)
for i in range(0,b+1):
    #print(i)
    if a.__contains__(str(i)):
        count += 1
        #print("count: ", count)
    else:
        count = 0
        break
if count == 0 or count > b+1 or count < b+1:
    print("no")
elif count == b+1:
    print("yes")
