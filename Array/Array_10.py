n,m = map(int,input().split())
list_n=[int(a) for a in input().split(" ",n-1)]
list_m=[int(b) for b in input().split(" ",m-1)]
list_n.sort()
list_m.sort(reverse=True)
output=""
for i in list_n:
    output = output + str(i) + " "
for j in list_m:
    output = output + str(j) + " "
print(output.rstrip())
