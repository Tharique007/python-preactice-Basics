a=input()
out=""
for i in a:
    if int(i)%2 != 0:
        out = out + i + " "

if len(out)>0:
    print(out.rstrip())
elif len(out)==0:
    print(-1)