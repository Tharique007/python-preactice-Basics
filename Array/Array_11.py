a=int(input(":"))
list1=[int(a) for a in input().split(" ",a-1)]
list_process =[]
frequency_list=[]
for i in list1:
    if i not in list_process:
        list_process.append(i)
for i in list_process:
    frequency_list.append(list1.count(i))

for j in range (0,len(frequency_list)):
    if frequency_list[j] == 2:
        print(list_process[j])