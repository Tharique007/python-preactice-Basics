#search using Binarymeathod

def binarysearch(array,x,low,high):
    while low <= high:
        mid=int((low+high)/2)
        print("mid",mid)
        if x == array[mid]:
            print("mid yes")
            return True
        elif x > array[mid]:
            print("right")
            low = mid+1
        elif x<array[mid]:
            print("left")
            high=mid-1

a,b=map(int,input().split(" "))
array1=[int(x) for  x in input().split(" ",a-1)]
array1.sort()
lw=0
hi=a-1

if binarysearch(array1,b,lw,hi):
    print("yes")
else:
    print("no")