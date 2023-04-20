"""
Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins.
 If it's a draw print 'D'.
Sample Testcase :
INPUT
R P
OUTPUT
P
"""


in1,in2=input("enter the selections").split(" ")

if (in1 == in2):
    print("D")
elif (in1 == "R" and in2 == "P") or (in1== "P" and in2 == "R" ):
    print("P")
elif (in1 == "P" and in2 == "S") or (in1== "S" and in2 == "P" ):
    print("S")
elif (in1 == "R" and in2 == "S") or (in1== "S" and in2 == "R" ):
    print("R")
