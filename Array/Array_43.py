A = int(input(":"))
list_of_books_exist = [int(serial) for serial in input().split(" ",A-1)]
B=int(input(":"))
lis_of_books_toadd= [int(serial) for serial in input().split(" ",B-1)]
list_of_books_exist.sort(reverse=True)
output=""
for i in lis_of_books_toadd:
    for j in range (0,(len(list_of_books_exist)-1)):
        if i <list_of_books_exist[j] and i >list_of_books_exist[j+1]:
            output=output+str(j+2)+" "
            break
    if i<list_of_books_exist[len(list_of_books_exist)-1]:
             output = output + str(len(list_of_books_exist) + 1) + " "
print(output.rstrip())