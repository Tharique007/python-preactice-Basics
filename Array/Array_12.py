a=int(input(":"))
list_in=[int(num) for num in input().split(" ",a-1)]
list_process=[]
for i in list_in:
    if i not in list_process:
        list_process.append(i)
list_freq=[]
output=""
for i in list_process:
    list_freq.append(list_in.count(i))

for j in range(0,len(list_freq)):
    if list_freq[j]>1:
        output = output + str(list_process[j])+" "

if len(output)>=1:
    print(output.rstrip())
else:
    print(-1)