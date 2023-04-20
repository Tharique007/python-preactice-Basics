input1=input()
vowles=["a","e","i","o","u"]
output=""
for i in input1:
    if i.lower() in vowles:
        input1=input1.replace(i,"")
if len(input1) > 0:
    output =input1[::-1]
    print(output)
else:
    print(-1)
