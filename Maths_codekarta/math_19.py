a=int(input(":"))
listin=[int(s) for s in input().split(" ",a-1)]
listin.sort()
def finestNumber(number):
    value=0
    tvalue = 1
    while value < number:
        tcube = tvalue**3
        tplus1cube = (tvalue + 1)**3
        value = tcube + tplus1cube
        if value == number:
            return True
            break
        tvalue +=1
    return False
output=[]
for i in listin:
    if finestNumber(i):
        output.append(i)
if len(output)>0:
    print(*output)
else:
    print(-1)