input1 = input()
length_of_string=len(input1)
output1=""

if length_of_string%2 == 0:
    for i in range(0,length_of_string):
        if i ==(length_of_string/2) or i==(length_of_string/2)-1:
            output1=output1+"*"
        else:
            output1=output1+input1[i]
elif length_of_string%2 != 0:
    for i in range(0,length_of_string):
        if i==int((length_of_string/2)):
            output1=output1+"*"
        else:
            output1=output1+input1[i]
print(output1)
