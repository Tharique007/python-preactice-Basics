a=int(input(":"))
content=[]
con_freq=[]
result=True

for i in str(a):
    if int(i) not in content:
        content.append(int(i))
print(content)
for j in content:
    a=str(a)
    con_freq.append(a.count(str(j)))
print(con_freq)

for i in range(1,len(con_freq)):
    if con_freq[i-1] != con_freq[i]:
        result = False
        break
if result:
    print(1)
else:
    print(0)
