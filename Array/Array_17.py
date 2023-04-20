a=int(input(":"))
list1=[str(num) for num in input().split(" ",(a*2)-1)]
list_salary=[]
output=""
for i in range(1,(a*2),2):
    list_salary.append(int(list1[i]))
list_salary.sort()
# print(list_salary)
for i in list_salary:
    for j in range(1,len(list1),2):
        if i == int(list1[j]):
            print(list1[j-1])