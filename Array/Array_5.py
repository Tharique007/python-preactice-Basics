str_in = input()
list1=[]
for i in str_in:
    list1.append(i)
#print(len(list1))
str_out = ""
for i in range(0,(len(list1)-1)):
    if list1[i] != list1[i+1] and list1[i] != " ":
        str_out += list1[i]
    elif list1[i] == list1[i+1]:
        list1[i] =" "
        list1[i+1]=" "

str_out += list1[len(list1)-1]
print(str_out)