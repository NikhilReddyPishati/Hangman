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
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")} #It is totally stored in dictionary 
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line) #it travels from first key-value pair to next value if guess is wrong

def dispaly_hint(hint):
    print(" ".join(hint)) #it displays hint but not included 

def dispaly_answer(choice):
    print(" ".join(choice)) #it displays choice but not included 



def main():
    choice = random.choice(words)
    hint =["_"]*len(choice)
    wrong_guesses=0
    guessed_letter = set()
    is_running = True
# main Function 

    while is_running:
        display_man(wrong_guesses)
        dispaly_hint(hint)
       
        guess = input ("Enter any letter").lower()
        if guess in choice:
            for i in range(len(choice)):
                if choice[i]== guess:
                    hint[i]=guess
                    continue
        else:
            wrong_guesses +=1
        
        if len(guess)>1 or guess.isdigit():
            print("invalid guess")
            continue
        if guess in guessed_letter:
            print("already guessed")
            continue
        guessed_letter.add(guess)

        if "_" not in hint:
            print(f"you wrong guesses are :{wrong_guesses}")
            print("YPU WIN!🏆🏆")
            is_running=False
        elif wrong_guesses>=len(hangman_art)-1:
            display_man(wrong_guesses)
            dispaly_answer(choice)
            print("YOU LOSE😭😭")
            is_running=False

            

if __name__ == "__main__":
    main()