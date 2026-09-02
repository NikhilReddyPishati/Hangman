import random          #imports random package
words="apple","banana","orange","pineapple","watermelon" #given words
print("Welcome to Hangman man").  #first print line
print("Instructions of the game\n1.You need to guess the word which are related to fruits Letter By Letter" \. #Instructions
"\n2.If your guess is wrong a human parts will appear on the screen"
"\n3.You need to guess the word before a total human is generated")
#All Three are Instructions 
#dictionary
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "  ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",#Used two Slashes because it takes input
                  "   "),
               5:(" o ",
                  "/|\\",#Used two Slashes because it takes input
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")} #These are Stored as Dictionary 
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line) #It travels from first key-value pair to next value if guess is wrong

def dispaly_hint(hint):
    print(" ".join(hint)) #It displays hint but not included 

def dispaly_answer(choice):
    print(" ".join(choice)) #It displays choice but not included 



def main():
    choice = random.choice(words) #chooses random words from Stored Inputs
    hint =["_"]*len(choice) #It Print dashes With Respect to Size of Words
    wrong_guesses=0
    guessed_letter = set()
    is_running = True
# main Function 

    while is_running:
        display_man(wrong_guesses) #Wrong guesses
        dispaly_hint(hint)
       # loop
        guess = input ("Enter any letter").lower().#It converts the input to Small letters
        if guess in choice:
            for i in range(len(choice)):#This is the loop where it include length of the choice
                if choice[i]== guess:#it compares the choice and guess
                    hint[i]=guess
                    continue #continues 
        else:
            wrong_guesses +=1 #it increase the count of wrong guesses
        
        if len(guess)>1 or guess.isdigit(): #it verifies whether equal or not
            print("invalid guess")#Displays the invalid guess 
            continue
        if guess in guessed_letter:
            print("already guessed")#displays this word
            continue
        guessed_letter.add(guess)

        if "_" not in hint:
            print(f"you wrong guesses are :{wrong_guesses}")
            print("YOU WIN!🏆🏆")#Displays the win text
            is_running=False
        elif wrong_guesses>=len(hangman_art)-1:
            display_man(wrong_guesses)
            dispaly_answer(choice)
            print("YOU LOSE😭😭")
            is_running=False

            

if __name__ == "__main__":
    main()