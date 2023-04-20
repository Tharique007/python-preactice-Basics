a=int(input(":"))
product=1
while a !=0:
    product *= a%10
    a=int(a/10)
print(product)