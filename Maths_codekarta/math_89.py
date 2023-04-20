def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def sum_of_factorila(numm):
    sum = 0
    for i in str(numm):
        sum += factorial(int(i))
    return sum

input1=int(input(":"))
result = False
start=1
while result == False:
    if sum_of_factorila(start) == input1:
        result = True
        break
    start +=1
if result:
    print(start)
else:
    print(-1)