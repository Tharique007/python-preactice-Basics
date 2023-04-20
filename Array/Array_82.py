a=int(input(":"))
b=str(bin(a))
#print(b)
count=0
for i in b[::-1]:
    count +=1
    if i == str(1):
        print(count)
        break
