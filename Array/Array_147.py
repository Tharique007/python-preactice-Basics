a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
result = False
for i in listin:
    if i%2 ==0:
        result = True
        break
if result:
    print("even")
else:
    print("odd")