month,year = str(input("Enter the month and year:")).split()
print(month)
print(year)
year_val = int(year)
leap_year = True
if (year_val%4 == 0 and year_val%100 !=0):
    leap_year = True
elif(year_val %400 == 0):
    leap_year = True
else:
    leap_year = False
normal_year_set = {"january":31, "febraury":28, "march":31, "April":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
if leap_year == True:
    normal_year_set["febraury"] = 29
else:
    pass

month_small=month.casefold()
value = normal_year_set.get(month_small)
days = 0
for i in range(1,(value+1)):
    #print("i=",i)
    count = 0
    for j in range(1,(i+1)):
        #print("j=",j)
        if i % j == 0:
            count = count + 1
            if count <= 2:
                continue
            else:
                print("days=",i)
                days = days
                break
print(days)
print((value-days))



