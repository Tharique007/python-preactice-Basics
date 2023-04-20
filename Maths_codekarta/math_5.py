a,b = str(input("Enter the two numbers:")).split(" ")
list_a= list(())
list_b= list(())
d = [int(a),int(b)]
count =0
#print(d)
if int(a)%2 != 0 or int(b)%2 !=0:
    for i in d:
        for j in range(1,(i+1)):
            if i%j == 0:
                if i == int(a):
                    list_a.append(j)
                else:
                    list_b.append(j)
else:
    print("0")
#print(list_a)
#print(list_b)
for i in list_a:
    if list_b.count(i) != 0:
        count = i
    else:
        continue
if count == 1:
    print("1")
else:
    print("0")


