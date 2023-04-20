string=input(":")
length=0
for i in string:
    if string.count(i) >length:
        length = string.count(i)
print(length)
