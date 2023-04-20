a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
output=[]
for i in listin:
    if listin.count(i) >1 and i not in output:
        output.append(i)

if len(output) > 0:
    output.sort()
    print(*output)
else:
    print("unique")