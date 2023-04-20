input1=input(":")
input2=input(":")
input3=input2
inp=""
inpz=""
turn=0
if len(input1) == len(input2):
    for i in input2:
        if turn<2:
            inp += i
            if input1.__contains__(inp):
                #print(inp)
                inpz = inp
            else:
                turn += 1
                input3 = input3.replace(inpz,"")
                inp=i
        else:
            break
#print(input3)
if input3 == inpz:
    print(1)
else:
    print(0)