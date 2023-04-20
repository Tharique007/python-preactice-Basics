a=int(input(":"))
listin=[int(s) for s in input().split(" ",a-1)]

for i in range(0,a):
    #print(min(listin[i:5]))
    d= min(listin[i:a])
    d_ind=listin.index(d)
    val=listin[i]
    listin[i] = d
    listin[d_ind] = val
    print(listin)
