a,b=map(int,input("a,b").split(" "))
list_in=[0]*(a*b)
list_in=[int(g) for g in input().split(" ",(a*b)-1)]
element = int(input(":"))
print(list_in)

if list_in.__contains__(element):
    print("yes")
else:
    print("no")