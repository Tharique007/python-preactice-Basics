"""
Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3
"""

a=int(input("enter the length of the array"))
list_in=[int(num) for num in input().split(" ",a-1)]
list_in_len = len(list_in)
print(list_in_len)
list_out=[0]*a
out_put=""
if list_in_len%2 == 0:
    for i in range(0,(list_in_len),2):
        list_out[i] = list_in[i+1]
        list_out[i+1]=list_in[i]
else:
    for i in range(0, (list_in_len-1), 2):
        list_out[i] = list_in[i + 1]
        list_out[i + 1] = list_in[i]
    list_out[list_in_len-1]=list_in[list_in_len-1]
for i in list_out:
    out_put = out_put + str(i)+" "
print(out_put.rstrip())