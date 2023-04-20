"""
Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).

Input Size : N <= 100000
Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
1 5
"""

N = int(input("enter the N value"))
n_list = [int(num) for num in input().split(" ",N-1)]
n_small = min(n_list)
n_big = max(n_list)
print(n_small,n_big)
ind_small=n_list.index(n_small)+1
ind_big = n_list.index(n_big)+1

print(ind_small,ind_big)