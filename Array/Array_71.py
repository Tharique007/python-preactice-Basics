a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
listout=[[],[]]
for i in list1:
    if i%2 == 0:
        listout[0].append(i)
    elif 1%2 != 0:
        listout[1].append(i)

if len(listout[0])==0 or len(listout[1]) == 0:
    print(-1)
elif len(listout[0]) > len(listout[1]):
    if len(listout[1]) == 1:
        print(*listout[1])
elif len(listout[0]) < len(listout[1]):
    if len(listout[0]) == 1:
        print(*listout[0])
