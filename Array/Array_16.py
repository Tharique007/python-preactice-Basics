a=int(input())
list_in=[int(num) for num in input().split(" ",a-1)]
list_process=[]
output_1=""
for i in range (0,len(list_in),2):
    list_process.append(list_in[i])
#print(list_process)
list_process.sort()
#print(list_process)
k=0
for j in range (0,len(list_in),2):
    if k<len(list_process):
        list_in[j] = list_process[k]
        k = k+1
#print(list_in)
for p in list_in:
    output_1 = output_1 + str(p)+" "
print(output_1.rstrip())


