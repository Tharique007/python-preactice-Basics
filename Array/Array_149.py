a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
result=max(listin)
num = 2
if listin.__contains__(1):
    print(1)
else:
    while num <= result:
        count = 0
        for i in listin:
            if i%num == 0:
                count += 1
            elif i%num != 0:
                break
        if count == len(listin):
            print(num)
            break
        else:
            if num <result:
                num +=1
            elif num == result:
                print(1)
                break