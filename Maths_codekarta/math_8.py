number = int(input("enter the number"))
num_str = str(number)
list_1 =[]
if len(num_str)>=2:
    for i in num_str:
        if list_1.count(i) == 0:
            list_1.append(i)
        else:
            continue

    if len(list_1)== 2:
        print("Saturated")
    else:
        print("Unsaturated")
else:
    print("Unsaturated")