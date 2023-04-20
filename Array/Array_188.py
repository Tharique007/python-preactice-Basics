a=int(input(":"))
sum=0
for i in str(a):
    sum += int(i)
result= "no"

if len(str(sum)) == 0:
    result="no"
elif len(str(sum)) == 1:
    result = "yes"
elif len(str(sum)) > 1:
    revee = str(sum)[::-1]
    if str(sum) == revee:
        result="yes"
print(result)