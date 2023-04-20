a=int(input(":"))
value=[]
result=False
for i in str(a):
    if int(i) not in value:
        value.append(int(i))
    else:
        print("yes")
        result = True
        break
if result == False:
    print("no")