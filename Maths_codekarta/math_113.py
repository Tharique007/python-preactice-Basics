a=int(input(":"))

def decimaltobin(num):
    return bin(num).lstrip("0b")
print(decimaltobin(a))
print(len(decimaltobin(a)))