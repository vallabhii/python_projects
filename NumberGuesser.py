response="a"
print("Let's play a game! Think of a number and I will try to guess what you're thinking of!\nEnter a range from which your number is in,\nthe number must be between the highest and lowest numbers,\nit cannot be equal to either of them.")
a=0
while a!=1: 
    b=0
    low=int(input("Enter the lower limit of range: "))
    high=int(input("Enter the higher limit of the range: "))
    while b!=1:  
        b=0
        if high<=low+1:
            print("That is not possible, lets start over.")
            b=1
        else:
            guess=(low+high)//2
            print("Is you number higher, lower or equal to ", guess)
            response=input("Enter \"h\" for higher, \"l\" for lower, and \"e\" for equal: ")
            if response=="h":
                low=guess
            elif response=="l":
                high=guess
            elif response=="e":
                print("Yayyy!")
                c=0
                while c!=1:
                    c=0
                    status=input("Would you like to keep playing? Enter \"y\" for yes and \"n\" for no: ")
                    if status=="n":
                        print("Thank you for playing the number guessing game, hope you had fun!")
                        a,b,c=1,1,1
                    elif status=="y":
                        b,c=1,1
                    else:
                        print("Please enter a valid respone.")
            else:
                print("Please enter a valid response.")
