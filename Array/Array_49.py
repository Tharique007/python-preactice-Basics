a=int(input(":"))
list_in=[int(num) for num in input().split(" ",a-1)]
sum=0
for i in range(a-3,a):
    sum += list_in[i]
#print(sum)
output=""
for i in list_in:
    difference= i - sum
    output = output+str(difference)+" "
print(output.rstrip())