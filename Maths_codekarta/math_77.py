#0.5 * [x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)]
listin=[]
for i in range(0,3):
    listin.append([int(n) for n in input(":").split(" ",2-1)])
x1=listin[0][0]
x2=listin[1][0]
x3=listin[2][0]
y1=listin[0][1]
y2=listin[1][1]
y3=listin[2][1]
value=(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
print(value)

if value==0:
    print("yes")
else:
    print("no")