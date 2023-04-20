a=int(input(":"))
list_in=[int(num) for num in input().split(" ",a-1)]
minimum = min(list_in)
output1="Dealer"
for i in range(0,a):
    if list_in[i] == minimum:
        output1=output1+str(i)
print(output1)