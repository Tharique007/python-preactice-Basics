a=int(input(":"))
listin=[int(num) for num in input().split(" ",a-1)]
listprocess = listin.copy()
output=""

for i in range(0,a):
    #print(listin[listin[i]])
    listprocess[i] = listin[listin[i]]
for i in listprocess:
    output = output + str(i) + " "
print(output.rstrip())