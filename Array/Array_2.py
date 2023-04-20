a=int(input(":"))
list_in = [int(num) for num in input().split(" ",a-1)]
list_process=[]
frequency_list=[]
outpout1=""

for i in list_in:
    if i not in list_process:
        list_process.append(i)
for i in list_process:
    frequency_list.append(list_in.count(i))
list_process.sort()
print(list_process)
print(frequency_list)

maximun_frequency = max(frequency_list)
for i in range (1,(maximun_frequency+1)):
    check=[]
    for j in range (0,len(frequency_list)):
        if frequency_list[j] == i:
            check.append(j)
    for k in check:
        outpout1 = outpout1 + str(list_process[k]) + " "

print(outpout1.rstrip())