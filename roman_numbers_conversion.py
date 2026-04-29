symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
subs={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
thousands=0
hundereds=0
tens=0
ones=0
int_num_list=[]
invalid_rom_num=False
a=input("Enter roman number")
rom_num=a.upper()
rom_num_list=list(rom_num)
rom_num_values=[]
for i in range(len(rom_num_list)):
    if rom_num_list[i] in list(symbols.keys()):
        rom_num_values.append(symbols[rom_num_list[i]])
        print(rom_num_values)
    else:
        invalid_rom_num=True
        break
if invalid_rom_num==False:
    print("gi")
    for j in range(1,len(rom_num_values)):
        if rom_num_values[j-1]<rom_num_values[j]: 
            if rom_num_list[j-1]+rom_num_list[j] in list(subs.keys()):
                rom_num_values[j]=subs[rom_num_list[j-1]+rom_num_list[j]]
                rom_num_list[j]=rom_num_list[j-1]+rom_num_list[j]
                rom_num_list.pop(j-1)
                rom_num_values.pop(j-1)
                j-=1
            else:
                invalid_rom_num=True
        if i<=len(rom_num_values)-2 and rom_num_values[j-1]==rom_num_values[j] and rom_num_values[j]==rom_num_values[j+1]:
            if rom_num_values[j] in ["I","X","C","M"]:
                