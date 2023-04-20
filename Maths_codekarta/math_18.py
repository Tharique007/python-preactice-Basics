a=int(input(":"))
count=0
def palindron(number):
    reverse = str(number)[::-1]
    if number == int(reverse):
        return True
    else:
        return False

for i in range (1,a+1):
    if palindron(i):
        count +=1
print(count)
