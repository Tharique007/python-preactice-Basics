a=int(input(":"))
def if_even(number):
    if number%2==0:
        return True
    else:
        return False
number_of_even=0
start=1
value=0

while number_of_even < a:
    if if_even(start):
        number_of_even +=1
        value += start
    start +=1
print(value)