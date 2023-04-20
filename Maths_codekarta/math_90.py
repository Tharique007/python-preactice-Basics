input1=int(input(":"))
sum_of_first_2digit=int(str(input1)[0])+int(str(input1)[1])
#print(sum_of_first_2digit)

if str(sum_of_first_2digit) in str(input1):
    print(1)
else:
    print(0)