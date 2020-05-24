import sys

def play():
    print("Play quiz")

def addQuestion():
    print("Adding a question")

def exitFunction():
    print("Exit")
    sys.exit(0)

if __name__ == "__main__":
    choice = 1
    while choice != 3:
        print("Quiz")
        print("-----")
        choice = int(input("Enter the choice:"))
        if choice == 1:
            play()
        elif choice == 2:
            addQuestion()
        elif choice == 3:
            exitFunction()
        else:
            print("Wrong")
        

