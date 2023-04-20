a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
output="no"
for i in range(0,a-2,2):
    print("I: ", i)
    if list1[i] < list1[i+1] and list1[i+1]>list1[i+2]:
        output = "yes"
    else:
        output = "no"
        print("no")
        break
if output == "yes":
    print("yes")

