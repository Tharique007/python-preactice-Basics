a=int(input(":"))
listiin=[int(n)for n in input().split(" ",a-1)]
listiin.sort()
for i in range(0,len(listiin)):
    if listiin[i] != i+1:
        print(i+1)
        break