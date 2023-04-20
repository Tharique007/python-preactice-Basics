a=int(input(":"))
list1=[int(num) for num in input().split(" ",a-1)]
minimum = min(list1)
maximum = max(list1)

output1=(list1.index(maximum))-(list1.index(minimum))
print(output1)
