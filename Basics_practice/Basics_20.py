"""
Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata

OUTPUT
ocedakat
"""

input_str=str(input("enter the striing"))
slen=len(input_str)
out_str=""
if slen % 2 == 0:
    for i in range(0,slen,2):
        out_str = out_str + input_str[(i+1)]
        out_str = out_str + input_str[(i)]

else:
    for i in range(0,(slen-1),2):
        out_str = out_str + input_str[(i+1)]
        out_str = out_str + input_str[(i)]
    out_str = out_str + input_str[(slen-1)]
print(out_str)