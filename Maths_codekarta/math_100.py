a,b=map(int,input(":").split(" "))
result=False
power=b
while result == False:
    if power<a:
        power *=b
        if power == a:
            result = True
            break
    else:
        break
if result:
    print("yes")
else:
    print("no")