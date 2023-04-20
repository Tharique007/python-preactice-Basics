a,b=map(int,input().split(" "))

def primenumber(num):
    if num <=1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def binary(nu):
    N = bin(nu)
    return (N.lstrip("0b"))

count = 0
for i in range(a,b+1):
    win=binary(i).count("1")
    #print(binary(i),":",win)
    if primenumber(win):
        count += 1
print(count)