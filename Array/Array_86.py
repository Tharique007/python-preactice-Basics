a=int(input(":"))
#print(a)
list1=[]
for i in range(0,a):
    list1.append(input())
#print(list1)
count=0
for i in range(1,a):
    if list1[i] == list1[i-1]:
        count += 1
if count > 0:
    print("yes")
else:
    print("no")
