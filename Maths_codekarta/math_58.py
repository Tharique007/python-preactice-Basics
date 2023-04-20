a=int(input(":"))
start=3
firstincrement=17
increment = 26
value=0
if a == 1:
    print(start)
elif a == 2:
    print((start + firstincrement))
elif a>2:
    for i in range(0,a):
        if i == 0:
            value += start
        elif i == 1:
            value += firstincrement
        elif i >=2:
            value += (firstincrement+increment)
            firstincrement = (firstincrement+increment)
            increment += 12
    print(value)
