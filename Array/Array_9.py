a=int(input("enter the length: "))
list_in = [int(num) for num in input().split(" ",a-1)]
list_process = []
out=""
for i in list_in:
    if i not in list_process:
        list_process.append(i)
list_process.sort(reverse=True)
# print(list_process)
list_frequency = []
for i in list_process:
    list_frequency.append(list_in.count(i))
# print(list_frequency)

for i in range(0,len(list_frequency)):
    if list_frequency[i] == 1:
        out = out + str(list_process[i])+" "

print(out.rstrip())