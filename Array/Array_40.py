string_in = input(":")
string_s=input("S:")
x=string_in.casefold()
y=string_s.casefold()
if x.count(y)>0:
    print(x.count(y))
elif x.count(y) == 0:
    print(-1)