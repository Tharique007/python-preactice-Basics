"""
Write a code get an integer number as input and print the odd and even digits of the number separately.

Input Description:
A single line containing an integer.

Output Description:
Print the even and odd integers of the integer in a separate line.

Sample Input :
1234
Sample Output :
2 4
1 3
"""
a=int(input())
b=str(a)
even = []
odd = []
even_out=""
odd_out=""
for i in b:
    if int(i)%2==0:
        even.append(int(i))
    else:
        odd.append(int(i))
even.sort()
odd.sort()

for i in even:
    even_out = even_out+str(i)+" "
for j in odd:
    odd_out = odd_out+str(j)+" "

print(even_out.rstrip())
print(odd_out.rstrip())