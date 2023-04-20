a=int(input(":"))
list1=[int(num) for num in input(":").split(" ",a-1)]
maximum=0
for i in range(1,a):
    if (list1[i]+list1[i-1]) > maximum:
        maximum = (list1[i]+list1[i-1])
print(maximum)