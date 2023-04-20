N=int(input(":"))
list_n=[int(num) for num in input().split(" ",N-1)]
T=int(input("="))
list_t=[int(t) for t in input().split(" ",T-1)]
output=""
for i in list_t:
    if list_n.count(i) >0:
        output = output+str(list_n.count(i))+" "
    elif list_n.count(i) == 0:
        output = output + "Not Present" + " "
print(output.rstrip())