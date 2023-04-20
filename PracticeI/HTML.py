from datetime import datetime
print(datetime.now())
time=str(datetime.now())
list = time.split(" ")
timing= str(list[1])
print(timing)
hrs_list=timing.split(":")
print(hrs_list)
hrs=int(hrs_list[0])
if hrs>=4 and hrs<12:
    print("good morning")
    document.
elif hrs>12 and hrs<18:
    print("good eve")
else:
    print("good night")