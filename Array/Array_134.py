a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
from functools import reduce

results = reduce((lambda x,y:x^y),list1)
print(results)