symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
valid_sub={"I":["V","X"],"X":["L","C"],"C":["D","M"]}
print("Converting roman number into integer.")
playagain="y"
while playagain.lower()=="y":
    error=True
    while error==True:  
        a=input("Enter roman number: ")
        b=a.upper()
        c=list(symbols.keys())
        number=[]
        for i in range(len(b)):
            if b[i] not in c:
                print(b[i], " does not exist in the roman number system.")
            elif len(b)-i>1 and b[i] in list(valid_sub.keys()) and b[i+1] in c and b[i+1] not in valid_sub[b[i]] and symbols[b[i]]<symbols[b[i+1]]:
                print("I can be subtracted  from V and X, X can be subtracted from L and C and, C can be subtracted from D and M.\nSo, ",b[i]," cannot be subtracted from ",b[i+1],".")
            elif i>=2 and b[i-1] in c and b[i-2] in c and symbols[b[i-1]]<symbols[b[i]] and symbols[b[i-2]]<=symbols[b[i-1]]:
                print("You cannot subtract two numbers from one number.")
            elif len(b)-i>=4 and [b[i+1],b[i+2],b[i+3]]==[b[i],b[i],b[i]]:
                print("Each symbol cannot be used more than 3 times consecutively.\nYou used ",b[i]," more than 3 times consecutively")
            elif len(b)-i>=2 and b[i] in ["V","L","D"] and b[i+1] in c and b[i]==b[i+1]:
                print("V, L and D cannot be repeated")
            elif len(b)-i>=2 and b[i] in ["V","L","D"] and b[i+1] in c and symbols[b[i]]<symbols[b[i+1]]:
                print("V, L and D cannot be subtracted")
            else:
                number.append(b[i])
        if len(number)==len(b):
            error=False
        else:
            print("Please enter a valid roman number.")
    integer=0
    for i in range(len(number)):
        if i>=1 and symbols[number[i-1]]<symbols[number[i]]:
            integer=integer+symbols[number[i]]-2*symbols[number[i-1]]
        else:
            integer+=symbols[number[i]]
    print("The integer for of the given roman number is ", integer)
    while True:
        playagain=input("Would you like to convert another number? Enter \"y\" for yes and \"n\" for no: ")
        if playagain.lower()=="y":
            break
        elif playagain.lower()=="n":
            print("Thank you for using the roman number conversion program, Hope you enjoyed!")
            break
        else:
            print("Please enter a valid response.")