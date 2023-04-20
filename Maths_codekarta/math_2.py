n=int(input("enter the number of Month:"))
principle = 1000
month_a = 1000
month_b= 1000
dummy=0
savings=0

for i in range(1,(n+1)):
    if i == 1:
            savings = principle+month_a
           # month_a = savings
    else:
        dummy = month_a+month_b
        savings = dummy+savings
        month_a = month_b
        month_b = dummy
print(savings)
