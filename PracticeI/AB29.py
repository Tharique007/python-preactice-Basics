a=int(input("b: "))
b=str(a)
even = []
odd = []
even_out=""
odd_out=""
for i in b:
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
even.sort()
odd.sort()

for i in even:
    even_out = even_out+str(i)+" "
for j in odd:
    odd_out = odd_out+str(j)+" "

print(even_out.rstrip())
print(odd_out.rstrip())