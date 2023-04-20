n = int(input("enter the number "))
n_str = str(n)
sum_ = 0
prod =1
for i in n_str:
    sum_ += int(i)
    prod *= int(i)
if (sum_ + prod) == n:
    print("Great")
else:
    print("no")


