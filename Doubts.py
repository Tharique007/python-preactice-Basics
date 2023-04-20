a= int(input("input:::: "))
b=str(a)
even=""
odd=""
for i in b:
    if (int(i)%2)==0:
        even= even+i
    else:
        odd= odd+i
for c in even:
    print(int(c), end=" ")
print()
for d in odd:
    print(int(d), end=" ")
