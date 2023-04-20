num=31
n=1
count=0
while n<=num:
    if n%2 !=0 and n%3 != 0:
        count += 1
    n +=1
print(count)