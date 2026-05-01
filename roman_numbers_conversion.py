symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
subs={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
runagain="y"
while runagain=="y":
    hundreds_sub,tens_sub,ones_sub=False,False,False
    ones,fives,tens,fifties,hundreds,fivehundreds,thousands=0,0,0,0,0,0,0
    int_num_list=[]
    invalid_rom_num=False
    a=input("Enter roman number: ")
    rom_num=a.upper()
    rom_num_list=list(rom_num)
    rom_num_values=[]
    for i in range(len(rom_num_list)):
        if rom_num_list[i] in list(symbols.keys()):
            rom_num_values.append(symbols[rom_num_list[i]])
        else:
            invalid_rom_num=True
            break
    if invalid_rom_num==False:
        length=len(rom_num_values)
        a=0
        while a<length-1:
            a+=1
            if rom_num_values[a-1]<rom_num_values[a]: 
                if rom_num_list[a-1]+rom_num_list[a] in list(subs.keys()):
                    rom_num_values[a]=subs[rom_num_list[a-1]+rom_num_list[a]]
                    rom_num_list[a]=rom_num_list[a-1]+rom_num_list[a]
                    rom_num_list.pop(a-1)
                    rom_num_values.pop(a-1)
                    a-=1
                    length-=1
                    if rom_num_values[a]<10:
                        ones_sub=True
                    elif rom_num_values[a]<100:
                        tens_sub=True
                    elif rom_num_values[a]<1000:
                        hundreds_sub=True
                else:
                    invalid_rom_num=True
                    break
    if invalid_rom_num==False:               
        for j in range(len(rom_num_values)):
            if rom_num_values[j]==1:
                ones+=1
            elif rom_num_values[j]==5:
                fives+=1
            elif rom_num_values[j]==10:
                tens+=1
            elif rom_num_values[j]==50:
                fifties+=1
            elif rom_num_values[j]==100:
                hundreds+=1
            elif rom_num_values[j]==500:
                fivehundreds+=1
            elif rom_num_values[j]==1000:
                thousands+=1
        if (ones_sub and ones>1) or (tens_sub and tens>1) or (hundreds_sub and hundreds>1):
            invalid_rom_num=True
        elif (ones>3 and fives!=1) or (tens>3 and fifties!=1) or (hundreds>3 and fivehundreds!=1) or thousands>3:
            invalid_rom_num=True
        elif fives>1 or fifties>1 or fivehundreds>1:
            invalid_rom_num=True
    if invalid_rom_num==True:
        print("Invalid roman number, please try again.")
    else:
        print("The integer form of ","".join(rom_num_list)," is ",sum(rom_num_values),".")
        while True:
            runagain=input("Would you like to find the integer value of another roman number? Enter \"y\" for yes and \"n\" for no: ")
            if runagain in ["y","n"]:
                break
            else:
                print("Please enter a valid response")