a=int(input(":"))
result=False
for i in range(2,a):
    if a%i==0:
        result = True
        break

if result:
    print("yes")
else:
    print("no")
