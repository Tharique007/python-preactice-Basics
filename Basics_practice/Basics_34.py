list1 = input("enter two words").split(" ")
word_out=""
print(list1)
for i in range((len(list1)-1),-1,-1):
   word_out= word_out + list1[i] + " "
print(word_out.rstrip())