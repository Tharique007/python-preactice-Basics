n,k=map(int,input(":").split(" "))
npk=1
for i in range((n-k)+1,n+1):
    npk *= i
rfact=1
for i in range(1,k+1):
    rfact *= i
print(int(npk/rfact))