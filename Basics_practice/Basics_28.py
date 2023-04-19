str = input("enter the string ")
str_out=""
for i in str:
    #print(ord(i))
    if ord(i) == 32:
        continue
    elif ord(i) in range(48,58):
        continue
    elif ord(i) in range(119,123):
       # print(chr((ord(i)+23)))
        str_out = str_out + chr((ord(i)-22))
    elif ord(i) in range(87,91):
        #print(chr(ord(i)+23))
        str_out = str_out + chr((ord(i) - 22))
    elif ord(i) in range(97,119):
#        print(chr(ord(i)-3))
        str_out = str_out +chr(ord(i)+4)
    elif ord(i) in range(65,87):
#        print(chr(ord(i)-3))
        str_out = str_out + chr(ord(i) + 4)

print(str_out)