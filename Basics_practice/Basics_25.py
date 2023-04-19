a1,b2=str(input("Enter the twwo number")).split(" ")
a= int(a1)
b= int(b2)
string =""
string2=""

while (a//10)>0 and (b//10)>0:
    if a>9 and b>9:
        c = (a%10)+(b%10)
        if c>9:
            string = string + str(c%10)
        else:
            string = string + str(c)
        a= a//10
        b= b//10

if (a+b) > 9:
    string = string + str((a+b)%10)
else:
    string = string + str((a + b))

x = len(string)+1
for i in range(-1,-x,-1):
    string2 = string2 + string[i]

print(int(string2))

string3=""
for i in string[::-1]:
    string3 =string3+i

print(int(string3))