a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
list1.sort()
difference=1
for i in range(0,a):
    for j in range(1,a):
        if abs(list1[i]-list1[j]) > difference:
            difference = abs(list1[i]-list1[j])
print(difference)