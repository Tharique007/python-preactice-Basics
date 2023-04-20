a=int(input(":"))
list_in=[num for num in input().split(" ",a-1)]
out1=[]
outfinal=""
for i in list_in:
    if i not in out1:
        out1.append(i)
for j in out1:
    outfinal = outfinal + j + " "
print(outfinal.rstrip())