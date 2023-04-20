inputin=input(":")
#inputin=inputin.rstrip(".")
listin=inputin.split(" ")
maximum=0
for i in listin:
    if i.isnumeric():
        if int(i) > maximum:
            maximum= int(i)
    elif i.__contains__("."):
        if i.rstrip(".").isnumeric():
            if int(i.rstrip(".")) > maximum:
                maximum = int(i.rstrip("."))
print(maximum)