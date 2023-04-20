a,b=[int(a) for a in input("enter:").split()]
c=[]*a
c=[int(c) for c in input().split()]
x={}
for i in range(b):
    e,f=[int(e) for e in input().split()]
    x[e]=f

print(x)
print("done")
y=x.keys()
print(y)

z=x.values()
print(z)
print(len(x))
for j in range(len(x)):
 pass