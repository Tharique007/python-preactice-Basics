"""
The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.
 It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.
For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to
 communicate with his officials.For the given input string(S) and shift print the encrypted string.

Sample Testcase :
INPUT
ABCdEFGHIJKLMNOPQRSTUVWXYz 23
OUTPUT
XYZaBCDEFGHIJKLMNOPQRSTUVw
"""


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