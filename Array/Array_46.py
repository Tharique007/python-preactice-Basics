a=int(input(":"))
list_in=[int(num) for num in input().split(" ",a-1)]
output=""
list_out=[0]*a
'''if len(list_in)%2 == 0:
    for i in range(0,len(list_in),2):
        minimum = min(list_in[i:len(list_in)])
        maximum = max(list_in[i:len(list_in)])
        indexofmin=list_in.index(minimum)
        indexofmax=list_in.index(maximum)
        #print(minimum, indexofmin)
        #print(maximum,indexofmax)
        list_in[indexofmin]=list_in[i+1]
        list_in[indexofmax]=list_in[i]
        list_out[i+1]=minimum
        list_out[i]=maximum
elif len(list_in)%2 != 0:
    for i in range(0,len(list_in)-1,2):
        minimum = min(list_in[i:len(list_in)])
        maximum = max(list_in[i:len(list_in)])
        indexofmin=list_in.index(minimum)
        indexofmax=list_in.index(maximum)
        #print(minimum, indexofmin)
        #print(maximum,indexofmax)
        list_in[indexofmin]=list_in[i+1]
        list_in[indexofmax]=list_in[i]
        list_out[i+1]=minimum
        list_out[i]=maximum
#print(list_in)
    for i in list_in:
        if i not in list_out:
            list_out[len(list_out)-1]=i

for i in list_out:
    output = output+str(i)+" "
print(output)'''

for i in range(int(a/2)):
    minimum = min(list_in)
    maximum = max(list_in)
    indexofmin = list_in.index(minimum)
    indexofmax = list_in.index(maximum)
    list_in.remove(minimum)
    list_in.remove(maximum)
    output = output + str(maximum) +" "
    output = output + str(minimum) + " "
if len(list_in)>0:
    for i in list_in:
        output = output +str(i)+" "
        list_in.remove(i)
print(len(list_in))
print(list_in)
print(output.rstrip())