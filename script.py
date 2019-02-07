import randword
import randchar

x = randword.wordSelect()
wlen = len(x)
hints = wlen // 2
tries = hints * 2

def menu():
    choice ='0'
    global wlen
    global hints
    global tries
    while tries != 0:
        print("===GUESS THE WORD===")
        print("Your word has " + str(wlen) + " letters")
        print("You have " + str(hints) + " hints")
        print("You have " + str(tries) + " tries")
        print("Press 1 if you want a hint")
        print("Type your word if you want to guess")
        print("TYPE exit IF YOU WANT TO CLOSE THIS GAME")
        choice = input ("Please make a choice: ")

        if tries == 1:
            print("OUT OF TRIES")
            print("THE WORD WAS ")
            print(x)
            exit()
        elif choice == "exit":
            exit()
        elif choice == "1":
            ch = randchar.randCharFromStr(x)
            print(ch)
            hints = hints - 1
        elif len(choice) > 1 :
            if x == choice:
                print("CONGRATS YOU GOT IT!!!")
                exit()
            else:
                tries  = tries - 1


menu()
