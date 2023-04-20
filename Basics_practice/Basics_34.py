"""
Given a string S consisting of 2 words reverse the order of two words .
Input Size : |S| <= 10000000

Sample Testcase :

   INPUT
   hello world

   OUTPUT
   world hello
"""

list1 = input("enter two words").split(" ")
word_out=""
print(list1)
for i in range((len(list1)-1),-1,-1):
   word_out= word_out + list1[i] + " "
print(word_out.rstrip())