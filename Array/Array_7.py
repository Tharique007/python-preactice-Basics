n,m= map(int,input().split(" "))
list_in = [int(num)for num in input().split(" ",n-1)]
out_1 =""
for i in range(0,(len(list_in)-1)):
    if abs(list_in[i]-list_in[i+1]) > m:
        out_1 += "1"+" "
    else:
        out_1 += "0"+" "
if abs(list_in[0]-list_in[len(list_in)-1]) > m:
    out_1 += "1" + " "
else:
    out_1 += "0"+" "
print(out_1.rstrip())
