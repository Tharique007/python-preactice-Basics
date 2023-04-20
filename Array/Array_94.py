a=int(input(":"))
aarray=[]
for i in str(a):
    aarray.append(i)
aarray.sort(reverse=True)
result=""
for i in aarray:
    result +=str(i)
print(result)
