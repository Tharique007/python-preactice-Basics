a=int(input(":"))
listin=[int(n) for n in input("!").split(" ",a-1)]
listin.sort()
sum=listin[0]+listin[1]
print(sum)