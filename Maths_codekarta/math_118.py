a,b=map(int,input(":").split(" "))
#print(a^b)
#print(bin(a^b))
print(bin(a^b).lstrip("0b").count("1"))