inputin=input(":")
engineno=0
for i in inputin:
    if i.isnumeric():
        engineno += int(i)
print(engineno)