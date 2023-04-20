a=int(input(":"))
listin=[int(n) for n in input("!").split(" ",a-1)]
listin.sort()
output=0
for i in range(len(listin),0,-1):
    num = listin[i-1]*(10**(i-1))
    output += num
print(output)