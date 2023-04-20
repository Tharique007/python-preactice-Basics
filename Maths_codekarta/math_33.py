inputin=input(":")
inputin = inputin.lower()
listvowel=["a","e","i","o","u"]
weight=0
for i in inputin:
    if i in listvowel:
        weight += ord(i)
if weight%8 == 0:
    print(1)
else:
    print(0)
