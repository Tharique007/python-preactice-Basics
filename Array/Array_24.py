a=int(input(":"))
listin = [int(num) for num in input().split(" ",a-1)]
listin.sort(reverse=True)
output1=""
lisprocess=[]
count_list=[]
for i in listin:
    if i not in lisprocess:
        lisprocess.append(i)
for j in lisprocess:
    count_list.append(listin.count(j))
least = min(count_list)
for i in lisprocess:
    if listin.count(i)== least:
        output1 = output1 + str(i)+" "
print(output1.rstrip())