a=int(input(":"))
list1=[]
list_process=[]
output1=""
for i in range(0,a):
    list2=[int(inn) for inn in input().split(" ")]
    list1.append(list2)
#print(list1)
for i in list1:
    if i[0] == 2 and len(list_process)>0:
        output1 = output1 + str(min(list_process))+" "
    elif i[0] == 2 and len(list_process)==0:
        output1 = output1 + "-1" + " "
    elif i[0] ==1:
        list_process.append(i[1])
print(output1.rstrip())