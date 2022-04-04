import random

def welcome():
    print('Welcome to minesweeper!')

def show_number_of_mines():
    usr_in = input('Show number of mines? (y/N) ')
    if usr_in == 'y' or usr_in == 'Y':
        return True
    else:
        return False

def create_mines(mines_cheat):
    mines = random.randint(1, 10)
    if mines_cheat:
        print('Number of mines: {}'.format(mines))

def main():
    welcome()
    mines_cheat = show_number_of_mines()
    create_mines(mines_cheat)

if __name__ == '__main__':
    main()