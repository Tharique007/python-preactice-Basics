"""
Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
Sample Testcase :
INPUT
2 5
OUTPUT
3
"""

a1,b1=str(input("enter the range to be checked: ")).split(" ")
a=int(a1)
b=int(b1)
out = 0

def primenumber(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num > 3:
        count=0
        for i in range(1,num+1):
            if num%i == 0 and count <=2:
                count +=1
            elif count >2:
                return False
        if count <=2 and count !=0:
            return True

for i in range(a,(b+1)):
   if primenumber(i):
       out += 1
print(out)