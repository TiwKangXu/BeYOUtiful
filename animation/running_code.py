import random
import sys
import time

colors = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'reset': '\033[0m'
}

hide_cursor = '\033[?25l'
show_cursor = '\033[?25h'

with open("code.txt", "r") as file:
    with open("record.txt", "a") as record:
        for row in file:
            for char in row:
                # delay = random.uniform(0.001, 0.1)
                # time.sleep(delay)
                record.write(char)
                print(colors['green'] + char, end='', flush=True)
            

            sys.stdout.write(show_cursor)
            sys.stdout.write(colors['reset'])
            sys.stdout.flush()
