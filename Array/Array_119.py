a=int(input(":"))
listin=[int(n) for n in input().split(" ",a-1)]
mini = min(listin)
maxi = max(listin)

print(abs(listin.index(mini)-listin.index(maxi)))