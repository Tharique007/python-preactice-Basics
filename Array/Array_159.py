a=int(input(":"))
listin=[int(n) for n in input("@:").split(" ",a-1)]
tootal=0

for i in range(0,len(listin)-1):
    sum =0
    for j in range(i+1,len(listin)):
        sum +=listin[j]
    #print(sum)
    if sum > tootal:
        tootal = sum
print(tootal)