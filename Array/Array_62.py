a=int(input(":"))
list1=[int(n) for n in input().split(" ",a-1)]
freq_loc=0
freq=0
for i in range(1,a):
    #print(i,list1[i],list1[i-1])
    if list1[i] == list1[i-1]:
        freq += 1
    #print(freq)
    if (i == a-1) or (list1[i] != list1[i-1]):
        if freq >= freq_loc:
            freq_loc = freq
        freq = 0
if freq_loc == 0:
    print(-1)
elif freq_loc >0:
    print(freq_loc+1)