symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
print("Converting roman number into integer.")
error=False
while error!=True:  
    a=input("Enter roman number:")
    b=a.capitalize()
    c=list(symbols.keys)
    number=[]
    for i in range(len(b)):
        if b[i] not in c:
            print(b[i], " does not exist in the roman number system.")
        elif b[i] in c and i>=1 and b[i-1] in c and b[i] not in ["V","I"] and b[i-1] not in c[c.index(b[i])-2:]:
            print("I can be subtracted  from V and X, X can be subtracted from L and C and, C can be subtracted from D and M\nso, ",b[i-1]," cannot be subtracted from ",b[i],".")
        else:
