a=int(input(":"))
listout=[str(string) for string in input().split(" ",a-1)]
output1=""
'''print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))'''
small = listout[0][0].casefold()
#print(small)
for i in range(0,a):
    for j in range(i+1,a):
        if listout[i][0].casefold() > listout[j][0].casefold():
            change = listout[j]
            listout[j] = listout[i]
            listout[i] = change

for i in listout:
    output1=output1+i+" "
print(output1.rstrip())