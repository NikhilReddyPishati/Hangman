#This is just A Practice File with Multiple Mini Programs
#import random
# This Total Lines of code Are Just For Practice
'''lowest = 1
highest = 3
answer = random.randint(lowest,highest)
guesses = 0
is_running = True
print("python guessing game")
print(f"Select The Number Between {lowest} and {highest}")

while is_running:
    guess = input(f"Enter any Guess Between {lowest} and {highest} ::::")

    if guess.isdigit():
        guess = int(guess)
        guesses+= 1

        if guess<lowest or guess>highest:
            print ("out of range")
        elif guess < answer:
            print("Guessed number is less than answer, try again")
        elif guess > answer:
           print ("Guessed number is greater than answer, try again")
        else:
            print (f"Correct {guess}")
            print (f"Your Attempts are {guesses} to get  correct answer")
            is_running = False
    else:
        print("Invalid guess")'''
#● ┌ ─ ┐ │ └ ┘

'''def display_lawada(username,rate,shapes):
    print(f"Hello figure name is {username}")
    print(f"Rate of the figure is {rate} and saamanlu is {shapes}")


display_lawada(" 1 -samantha",31,"32,30,36")
display_lawada(" 2 -kaajal",33,"33,30,40")'''

'''import time
def count(end ,start=0):
    for lavawda in range (start,end):
        print(lavawda)
        time.sleep(1)
    print("Done")

count(11)
x =5
y=x
x=x+2
y=y+2
print(x+y)
print(help("modules"))



#ENCRYPTION OF INPUT AND DECRIPTION OF INPUT
import string
import random
mouse =" "+string.punctuation+string.ascii_letters+string.digits
mouse =list(mouse)
keys = mouse.copy()
random.shuffle(keys)
#print(f"main stings are {mouse}")
#print(f"keys are :{keys}")
#Encryption of data
input_data = input("enter your data")
encrypt_data =""
for letter in input_data:
    Index = mouse.index(letter)
    encrypt_data += keys[Index]
print(encrypt_data)
#Decryption of given message
input_data = input("Encrypted message")
decrypt_message=""
for letter in input_data:
    index = keys.index(letter)
    decrypt_message+= mouse[index]
print(f"decrypoted data is :{decrypt_message}")



#HANGMAN GAME
import random
words="apple","banana","orange","pineapple","watermelon"
print("Welcome to Hangman man")
print("Instructions of the game\n1.You need to guess the word which are related to fruits Letter By Letter" \
"\n2.If your guess is wrong a human parts will appear on the screen"
"\n3.You need to guess the word before a total human is generated")

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
                  "/|\",
                  "   "),
               5:(" o ",
                  "/|\",
                  "/  "),
               6:(" o ",
                  "/|\",
                  "/ \")}
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def dispaly_hint(hint):
    print(" ".join(hint))

def dispaly_answer(choice):
    print(" ".join(choice))


def main():
    choice = random.choice(words)
    hint =["_"]*len(choice)
    wrong_guesses=0
    guessed_letter = set()
    is_running = True


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
    main()'''
