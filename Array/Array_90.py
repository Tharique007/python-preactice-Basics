a,b=input(":").split()
a=str(a)
b = int(b)
if b>0:
    for i in range(b-1,len(a),b):
        a=a.replace(a[i],a[i].upper())
print(a)