a=int(input(":"))
sum =0
'''b=str(a)

for i in range(0,len(b)):
    if (i+1)%2 != 0:
        sum += int(b[i])
if sum % 2==0:
    print("E")
else:
    print("O")'''
a=int(input(":"))
sum =0
while a>0:
    sum += int(a%10)
    a=int(a/10)
if sum % 2==0:
    print("E")
else:
    print("O")