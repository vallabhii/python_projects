symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
valid_sub={"I":["V","X"],"X":["L","C"],"C":["D","M"]}
print("Converting roman number into integer.")
error=False
while error!=True:  
    a=input("Enter roman number:")
    b=a.capitalize()
    number=[]
    for i in range(len(b)):
        if b[i] not in list(symbols.keys()):
            print(b[i], " does not exist in the roman number system.")
        elif b[i] in list(valid_sub.keys()) and b[i+1] not in valid_sub[b[i]]:
            print("I can be subtracted  from V and X, X can be subtracted from L and C and, C can be subtracted from D and M\nso, ",b[i-1]," cannot be subtracted from ",b[i],".")
        else:
