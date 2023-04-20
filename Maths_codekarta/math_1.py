n=int(input("enter the number:"))
a=1
b=(n-1)
count = 0
for i in range(1,n):
    if ((a+b) == n):
        count = count+1
        #print("A=", a)
        #print("B=" , b)
        #print("count:", i , count)//
    a = a+1
    b = b-1
    #print("A=" , a)
    #print("B=" , b)
print(count)