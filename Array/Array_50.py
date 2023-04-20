a=int(input(":"))
list_in =[int(num) for num in input().split(" ",a-1)]
large_sum=list_in[0]
start_index=0
end_index=0

for i in range (0,a):
    for j in range(i,a):
        summing = sum(list_in[i:(j+1)])
        print(i,(j+1),summing)
        if summing > large_sum:
            large_sum = summing
            start_index = i
            end_index = j
print(large_sum)