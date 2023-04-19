N = int(input("enter the N value"))
n_list = [int(num) for num in input().split(" ",N-1)]
import math
n_small = min(n_list)
n_big = max(n_list)
print(n_small,n_big)
ind_small=n_list.index(n_small)+1
ind_big = n_list.index(n_big)+1

print(ind_small,ind_big)