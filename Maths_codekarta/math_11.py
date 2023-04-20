n=int(input("enter the number of employees: "))
m= n*3
inputs = [str(num) for num in input().split(" ",(m-1))]
print(inputs)
list_1987 = ["JANUARY","MARCH","MAY","JULY"]
list_1986 = ["JANUARY","MARCH","MAY","JULY","AUGUST","OCTOBER","DECEMBER"]
loop =0
count = 0
outputs=""
for i in range (2,(len(inputs)+1),3):
    k= inputs[i]
    l= inputs[(i-1)]
    m= inputs[(i-2)]
    if (int(k)<=1987):
        if (int(k)==1987 and list_1987.count(l.upper())!=0):
            if(l.upper()=="JULY" and int(m)<=22 and int(m)>0 ):
                loop += 1
                count +=1
                #print(loop, end=" ")
                outputs = outputs + str(loop) + " "
            elif(l.upper()!="JULY"):
                loop += 1
                count += 1
                #print(loop, end=" ")
                outputs = outputs + str(loop)+ " "
            else:
                loop += 1
        elif(int(k)<1987 and list_1986.count(l.upper())!=0):
            loop += 1
            count += 1
            #print(loop,end=" ")
            outputs = outputs + str(loop)+ " "
    else:
        loop += 1
#print("\b")
print(outputs.rstrip(" "))

if count == 0:
    print("-1")