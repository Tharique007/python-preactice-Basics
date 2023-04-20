a=int(input(":"))
listiin=[int(n) for n in input().split(" ",a-1)]
result = False
num = 1
#print(num)
while result == False:
    #print(num)
    count = 0
    for i in listiin:
        if num % i != 0:
            break
        elif num % i == 0:
            count += 1
    if count == len(listiin):
        print(num)
        result = True
    num +=1
