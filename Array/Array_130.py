string1=input()
count_1=0
count_2=0
for i in string1:
    if i == "(":
        count_1 += 1
    elif i == ")":
        count_2 += 1
    else:
        print("enter the string only using ()")
if count_1 == count_2:
    print("yes")
else:
    print("no")