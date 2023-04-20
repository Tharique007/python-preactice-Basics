a,b=map(int,input(":").split(" "))
freq=0

while a != 0:
    #print(a)
    if a%10 == b:
        freq += 1
    a = int(a/10)

#print(a)
if freq != 0:
    print(freq)
else:
    print(-1)