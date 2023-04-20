a = int(input("Enter the Number of tickets "))
list_in=[int(num) for num in input().split(" ",a-1)]
b=int(input("="))
final_outputs=""
#print(a)
#print(list_in)
#print(b)
output=[]
for i in list_in:
    if i%b ==0:
        output.append(1)
    else:
        output.append(0)
for j in output:
    final_outputs = final_outputs + str(j)+" "
print(final_outputs.rstrip(" "))