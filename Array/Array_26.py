a=int(input(":"))
listin=[int(num) for num in input().split(" ",a-1)]

length = len(listin)
if length >=3:
    lastsum = listin[length-1]+listin[length-2]+listin[length-3]
    firstsum = listin[0]+listin[1]+listin[2]
    if lastsum == firstsum:
        print("1")
    else:
        print("0")
else:
    print("0")