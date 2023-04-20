a=int(input())
list1=[int(num) for num in input().split(" ",a-1)]
minimum=min(list1)
for i in range(0,a):
    for j in range(i+1,a+1):
        #print(i, j, sum(list1[i:j]))
        if sum(list1[i:j])<minimum:
            minimum = sum(list1[i:j])
print(minimum)