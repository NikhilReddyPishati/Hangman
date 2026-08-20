#import random
# This Total Lines of code
'''lowest = 1
highest = 3
answer = random.randint(lowest,highest)
guesses = 0
is_running = True
print("python guessing game")
print(f"select number between {lowest} and {highest}")

while is_running:
    guess = input(f"enter any guess between {lowest} and {highest} ::::")

    if guess.isdigit():
        guess = int(guess)
        guesses+= 1

        if guess<lowest or guess>highest:
            print ("out of range")
        elif guess < answer:
            print("guessed number is less than answer, try again")
        elif guess > answer:
           print ("guessed number is greater than answer, try again")
        else:
            print (f"corect {guess}")
            print (f"your attempts are {guesses} to get  correct answer")
            is_running = False
    else:
        print("invalid guess")'''
#● ┌ ─ ┐ │ └ ┘

'''def display_lawada(username,rate,shapes):
    print(f"hello figure name is {username}")
    print(f"rate of the figure is {rate} and saamanlu is {shapes}")


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


#Banking project
import time
import datetime
def show_balance():
    show=int(input("please enter your secret 4 digit pin"))
    if show == pin:
        print(f"Available balance is ${balance}")
    else:
        print("wrong pin")
def withdraw():
    withdraw_amount=int(input("please enter amount "))
    if withdraw_amount > balance:
        print(f"Insufficient funds available balance is {balance}")
    elif withdraw_amount == balance:
        print(f"sorry sir/mam You need to maintain minimum balance and Available balance is {balance}")
    elif withdraw_amount < balance:
        pin = int(input("please enter your secret pin :"))
        if pin == pin:
            print(f"Amount withdrawed and available balance is:${balance-withdraw_amount}")
        else:
            print(f"Incorrect pin please start the process again")
def deposit():
    deposit_money = int(input("Please Enter the amount you want to deposit :$ "))
    pin = int(input("please enter your secret pin "))
    if pin == 0000:
            print(f"Amount deposited and available balance is:${balance+deposit_money}")
    else:
        print("Incorrect pin please start the process again")
def help():
    print("please contact bank@gmail.com")
date =datetime.datetime.now()
print(date)
balance = 5
pin = 0000
is_running = True
while is_running:
    time.sleep(1)
    print("welcome and Good Day")
    print("May i help you")
    print("1 = Showbalance ")
    print("2 = withdraw")
    print("3 = deposit  ") 
    print("4 = help   " )
    print("5 = Exit")
    choice = (input("Enter you choice from (1 - 5)"))
    if choice == '1':
        show_balance()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        deposit()
    elif choice == '4':
        help()
    elif choice == '5':
        is_running = False
    else:
        print("it is an invalid choice please try again")
print("Thank You")
n = 5
for rows in range(1,2*n):
    if rows<=2*n:
        for cols in range (1,rows+1):
            print("*",end="")
    else:
        print("tq")
        for cols in range (1,2*n-rows+1):
            print("&",end = "")
    print()
m=5
for rows in range(1,m+1):
    for cols in range(rows+1,m):
        print("*",end="")
    print()
for i in range(5,0,-1):
    print("*"*i)
m=5
for rows in range (m,0,-1):
    for cols in range(rows):
        print("*",end ="")
    print()
m=7
for rows in range(1,m+1):
    for cols in range (rows):
        print("*",end ="")
    print()
a=256
b=256
c=257
d=257
print(a is b,c is d)

def show_balance(balance):
    show=int(input("please enter your secret 4 digit pin"))
    if show == 0000:
        print(f"Available balance is ${balance}")
    else:
        print("wrong pin")
def withdraw(balance):
    withdraw_amount=float(input("please enter amount "))
    if withdraw_amount > balance:
        print(f"Insufficient funds available balance is {balance}")
    elif withdraw_amount == balance:
        print(f"sorry sir/mam You need to maintain minimum balance and Available balance is {balance}")
    elif withdraw_amount < balance:
        pin = int(input("please enter your secret pin :"))
        if pin == 0000 :
            print(f"Amount withdrawed and available balance is:${balance-withdraw_amount}")
        else:
            return withdraw_amount
def deposit(balance):
    amount = float(input("enter your deposit amount"))
    if amount <= 0:
        print("invalid amount")
        return 0
    else:
        return amount
def help():
    print("please contact bank@gmail.com")
#date =datetime.datetime.now()
#print(date)
def main():
    balance = 5
    is_running = True
    while is_running:
    #time.sleep(1)
        print("welcome and Good Day")
        print("May i help you")
        print("1 = Showbalance ")
        print("2 = withdraw")
        print("3 = deposit  ") 
        print("4 = help   " )
        print("5 = Exit")
        choice = (input("Enter you choice from (1 - 5)"))
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance -=withdraw(balance)
        elif choice == '3':
            balance += deposit(balance)
        elif choice == '4':
            help()
        elif choice == '5':
            is_running = False
        else:
            print("it is an invalid choice please try again")
    print("Thank You")
if __name__ == '__main__':
    main()
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
