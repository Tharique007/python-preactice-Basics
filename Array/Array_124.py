a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
mini =max(listin)

for i in range(0,(len(listin)-1)):
    for j in range(i+1, len(listin)):
        #print("i:", i,"j:",j)
        if abs(listin[i]-listin[j]) < mini:
            mini = abs(listin[i]-listin[j])
print(mini)

