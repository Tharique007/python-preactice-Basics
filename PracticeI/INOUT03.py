a1,b1=input().split()
list_1=[int(num) for num in input().split(" ",int(a1)-1)]
print(a1,b1)
out=""
for i in list_1:
    out=out+str(i)+" "
print(out.rstrip())
