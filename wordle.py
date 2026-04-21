from random_word import RandomWords
from wordfreq import zipf_frequency
r = RandomWords()
playagain=""
print("Lets play wordl!\nThe word is 5 alphabets long,\n🟩 Indicates that the alphabet is correct and in the right place,\n🟨 Indicates that the alphabet is in the word but in the wrong place,\n⬜️ Indicates that the alphabet is not in the word at all.\nYou get 7 attempts to guess the word!")
while playagain!="n":
    word=""
    while not word or len(word)!=5 or zipf_frequency(word, 'en')<=0:
        word = r.get_random_word()
    guess=""
    round=7
    while guess!=word and round!=0:
        wordlis=list(word)
        g=input("Guess the word: ")
        guess=g.lower()
        ans=[" ⬜️ "," ⬜️ "," ⬜️ "," ⬜️ "," ⬜️ "]
        if zipf_frequency(guess, 'en')>0 and len(guess)==5:
            for i in range(5):
                print(" ",guess[i],end=" ")
            print("")
            for i in range(5):
                if guess[i]==word[i] and guess[i] in wordlis:
                    ans[i]=" 🟩 "
                    wordlis.pop(wordlis.index(guess[i]))
            for i in range(5):
                if guess[i]!=word[i] and guess[i] in wordlis:
                    ans[i]=" 🟨 "
                    wordlis.pop(wordlis.index(guess[i]))
            for i in range(5):
                print(ans[i],end="")
            print("")
            round-=1
        elif zipf_frequency(guess, 'en')>0 and len(guess)!=5:
            print("This word is not 5 alphabets, please enter a valid word.")
        elif zipf_frequency(guess, 'en')<=0 and len(guess)==5:
            print("This word does not exist, please enter a valid word.")
        elif zipf_frequency(guess, 'en')<=0 and len(guess)!=5:
            print("This word does not exist, nor is it 5 alphabets, please enter a valid word.")
    if guess==word:
        print("Yayyyyy! You got it in ",7-round," tries!")
    else:
        print("Awn man, better luck next time!\nThe word was\'",word,"\'")
    a=0
    while a!=1:
        playagain=input("Would you like to play again? Enter \'y\' for yes and \'n\' for no: ")
        if playagain=="y":
            a=1
        elif  or playagain=="n":
            a=1
            print("Thank you for playing wordle! Hope you had fun.")
        else:
            print("Please enter a valid response.")
