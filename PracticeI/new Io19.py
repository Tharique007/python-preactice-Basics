A,B= [int(A)for A in input().split()]
big= 0
small = 0
reminder = 1
if A>B:
    big = A
    small = B
else:
    big = B
    small = A
while reminder !=0:
        if big%small==0:
            print(small)
            break
        else:
            reminder = big%small
            big = small
            small= reminder
print(small)
