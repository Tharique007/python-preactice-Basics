Num = int(input("Enter the number to be skipped: "))
start, end = map(int, input("Enter the range to be checked: ").split(" "))

for i in range(start, (end+1)):
    if i != Num:
        print(i, end=" ")
