import random,time

fruits=['mango','orange','kewi','grape','watermulon']
secret_word=random.choice(fruits)
guesses=0
def image(guesses):
    if guesses==0:
        print("_______\n"
              "|     |\n"
              "|\n"          
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "---------\n")
    elif guesses==1:
        print("_______\n"
              "|     |\n"
              "|     0\n"          
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "---------\n")

    elif guesses==2:
        print("_______\n"
              "|     |\n"
              "|     0\n"          
              "|    /\n"
              "|\n"
              "|\n"
              "|\n"
              "---------\n")
    if guesses==3:
        print("_______\n"
              "|     |\n"
              "|     0\n"          
              "|    / \ \n"
              "|\n"
              "|\n"
              "|\n"
              "---------\n")
    if guesses==4:
        print("_______\n"
              "|     |\n"
              "|     0\n"          
              "|    / \ \n"
              "|     |\n"
              "|\n"
              "|\n"
              "---------\n")

    if guesses==5:
        print("_______\n"
              "|     |\n"
              "|     0\n"          
              "|    / \ \n"
              "|     |\n"
              "|    /\n"
              "|\n"
              "---------\n")
    if guesses==6:
        print("_______\n"
              "|     |\n"
              "|     0\n"          
              "|    / \ \n"
              "|     |\n"
              "|    / \ \n"
              "|\n"
              "---------\n")

def hangman():
    guessed_letters=[]
    secret_word
    word=list(secret_word)
    guesses=0
    blanks = "_"*len(secret_word)
    blank_list=list(blanks)
    player=input("hello buddy,What is your name!\n")
    time.sleep(0.5)
    print(player+"! welcome to hangman game\n")
    time.sleep(0.5)
    image(guesses)
    print(blanks+"\n")
    guess=input("Please guess the letter\n")
    guess.lower()
    if len(guess)>1:
        print("You are allowed to enter only one word\n")
    elif guess=="":
        print("Please enter one word\n")
    elif guess in guessed_letters:
        print("You already entered this word please enter different letter\n")
        guessed_letters.append(guess)
    else:
        run=True
        while run:
            guessed_letters.append(guess)
            if guess in word:
                x=word.index(guess)
                blank_list[x]=guess
                print(blank_list)
                if blank_list==list(secret_word):
                    print("congratulations "+player+" You won the game\n")
                    run=False
                else:
                    guess=input("guess another word\n")
                    if len(guess)>1:
                        print("You are allowed to enter only one word\n")
                        guess=input("guess a word again\n")
                    elif guess=="":
                        print("please enter a text\n")
                        guess=input("Enter aword\n")
                    elif guess in guessed_letters:
                        print("You already entered this word please enter different letter\n")
                        guess=input("Enter different word\n")
                    else:
                        pass
            else:
                guesses+=1
                image(guesses)
                if guesses==6:
                    print("oops you lost the game\n")
                    run=False
                else:
                    guess=input("guess another word\n")
                    if len(guess)>1:
                        print("You are allowed to enter only one word")
                        guess=input("guess a word again\n")
                    elif guess=="":
                        print("please enter a text\n")
                        guess=input("Enter aword")
                    elif guess in guessed_letters:
                        print("You already entered this word please enter different letter\n")
                        guess=input("Enter different word\n")
                    else:
                        pass






    interest=input("if u want to play again press s\n")
    if interest=="s":
        hangman()
    else:
        print("Thanks for playing\n")         

hangman()
