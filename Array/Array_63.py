a=int(input())
list1=[]
for i in range(a):
    list1.append(input())
#print(list1)
#Inputs="kabali"
output=0
for i in list1:
    if i.count("k") == 1 and i.count("a")==2 and i.count("b")==1 and i.count("l") == 1 and i.count("i")==1:
        output += 1
print(output)
