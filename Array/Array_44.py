a=int(input(":"))
list_in=[int(value) for value in input().split(" ",a-1)]
for i in list_in:
    if list_in.count(i) == 1:
        print(i)