a=int(input(":"))

def hexatodecial(num):
    num = str(num).strip().upper()
    table={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    p=len(str(num))-1
    decimal=0
    for i in num:
        decimal += table[i] *(16**p)
        p -= 1
    return decimal
print(hexatodecial(a))