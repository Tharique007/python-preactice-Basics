input_1=input(":")
string_odd=""
string_even=""
for i in range(0,len(input_1)):
    if (i+1)%2 == 0:
        string_even=string_even+str(input_1[i])
    elif (i+1)%2 != 0:
        string_odd=string_odd+str(input_1[i])
print(string_odd,string_even)
