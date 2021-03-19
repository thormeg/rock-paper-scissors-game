"""
    Rock Paper Scissors Game
"""
import os
import random

from constants.ascii_art import (
    draw,
    lose,
    options,
    paper,
    rock,
    scissors,
    the_end,
    welcome,
    win
)

def determine_result(p, c, name):
    """Calculates if player wins or loses."""
    art = {
        'r': rock,
        'p': paper,
        's': scissors
    }

    print(f'{name} chose:\n\n{art[p]}')
    print('vs')
    print(art[c] + '\n\n')

    if p == c:
        print(draw)
        return
    
    if (p == 'r' and c == 's') or (p == 'p' and c == 'r') or (p == 's' and c == 'p'):
        print(win)
        return

    print(lose)


def main_loop(name):
    """Main loop."""
    valid_choices = ('r', 'p', 's')
    loop = True

    name = name if name else 'player'

    while loop:
        clear_screen()
        print(f'Welcome, {name}!\n')
        print(options)
        choice = input('Please pick [R]ock, [P]aper, or [S]cissors:\n')

        if choice.lower() in valid_choices:
            choice = choice.lower()
            computer = random.choice(valid_choices)
            determine_result(choice, computer, name)
        elif choice.lower() == 'q':
            return
        else:
            clear_screen()
            continue
        again = input('\n\nPlay again [Y/N]?\n')
        loop = again.upper() != 'N'
        

def main():
    """Entry point."""
    clear_screen()
    print(welcome)

    name = input('Enter your name: \n')

    main_loop(name)

    print(the_end)


def clear_screen():
    """Clears terminal screen."""
    os.system('clear')


if __name__ == '__main__':
    main()