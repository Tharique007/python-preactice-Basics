a=int(input(":"))
listin=[int(num) for num in input().split(" ",a-1)]
listin.sort(reverse=True)
print(listin[1])