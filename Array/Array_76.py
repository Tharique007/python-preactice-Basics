a=int(input(":"),2)
#print(a)
b=""
#print(oct(a))
while a>8:
    b += str(a % 8)
    a= int(a/8)
    if a <8:
        b += str(a)

print(int(b[::-1]))
