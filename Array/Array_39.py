m,n=map(int,input(":").split(" "))
list_in=[0]*m

for i in range (m):
   list_in[i] = [int(na) for na in input().split(" ",n-1)]
#print(list_in)
count_0=0
count_1=0

for i in range(m):
    for j in range(n):
        if list_in[i][j] == 0:
            count_0 += 1
        elif list_in[i][j] == 1:
            count_1 += 1
print("RAM:",count_0)
print("SITA:",count_1)