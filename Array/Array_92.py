a=int(input())
print(bin(a).lstrip("0b"))
print(int(bin(a).lstrip("0b"),2))