import random

def win():
    print("__________________________________________________________________________\n")
    print("\ \  / /  / ___ \  | |  | |   | |          | |  |__ __| | |\ \  | |   | |")
    print(" \ \/ /  | |   | | | |  | |   | |  / /\ \  | |    | |   | | \ \ | |   |_|")
    print("  |  |   | |___| | | |__| |    \ \/ /  \ \/ /    _| |_  | |  \ \| |    _ ")
    print("  |__|    \_____/  \_____/      \__/    \__/    |_____| |_|   \___|   |_|\n")
    print("__________________________________________________________________________\n")

def lose():
    print("__________________________________________________________________________\n")
    print("\ \  / /  / ___ \  | |  | |   | |     / ___ \  / ____|  |  ___| | |")
    print(" \ \/ /  | |   | | | |  | |   | |    | |   | | \ \___   | |__   |_|")
    print("  |  |   | |___| | | |__| |   | |___ | |___| |  \___ \  |  __|   _ ")
    print("  |__|    \_____/  \_____/    |_____| \_____/  |______/ |_____| |_|\n")
    print("__________________________________________________________________________\n")

def draw():
    print("__________________________________________________________________________\n")
    print("|  __ \   |  __ \    /   \   | |          | | | |")
    print("| |  \ \  | |__\ |  / /_\ \  | |  / /\ \  | | |_|")
    print("| |___| | | __  /  |  ___  |  \ \/ /  \ \/ /   _ ")
    print("|______/  |_| \_\  | |   | |   \__/    \__/   |_|\n")
    print("__________________________________________________________________________\n")

def game_over():
    print("\n->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print("/ ___ \   /   \  |  \      /  | | ____|  /  _  \   | |   | | | ____| |  _  \ ")
    print("| |  |_| / / \ \ |   \    / | | | |__   / /   \ \  | |   | | | |__   | | \ |")
    print("| ||__ | | |_| | | |\ \  / /| | |  __| | |     | | \ \   / / |  __|  | |_/ /")
    print("| |__| | |  _  | | | \ \/ / | | | |___  \ \___/ /   \ \_/ /  | |___  | |\ \ ")
    print("\_____/  | | | | |_|  \__/  |_| |_____|  \_____/     \___/   |_____| |_| \_\ ")
    print("-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<")

def game():
    signs = ['blank', 'ROCK', 'PAPER', 'SCISSORS']
    opp_sign = []
    opp_sign.append(random.randint(1, 3))
    number = opp_sign[0]
    print("_________________________________")
    print('ROCK, PAPER, SCISSORS. SHOOT!!!' '\n','Please choose between: ', '\n','[ROCK] [PAPER] [SCISSORS]','\n' '  (1)     (2)      (3)')
    print("_________________________________")

    try:
        user_sign = int(input('Make your choice: '))

        print('You:', '\t', '\t', (signs[user_sign]))
        print('Opponent:', '\t', (signs[number]))

        if user_sign == 1 and number == 3:
            win()
        elif user_sign == 1 and number == 2:
            lose()
        elif user_sign == 2 and number == 1:
            win()
        elif user_sign == 2 and number == 3:
            lose()
        elif user_sign == 3 and number == 2:
            win()
        elif user_sign == 3 and number == 1:
            lose()
        else:
            draw()
    except ValueError:
        print("Invalid Information Entered!\n")
    except IndexError:
        print("Invalid Information Entered!\n")

def restart():
    try:
        play_again = str(input("Would you like to play again? (y/n): "))

        if play_again == 'y':
            game()
        elif play_again == 'n':
            game_over()
            exit()
        else:
            print("Invalid Information Entered!")
    except ValueError:
        print("Invalid Information Entered!\n")

game()
while True:
    restart()

