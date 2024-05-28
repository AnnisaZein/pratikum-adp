from termcolor import colored, cprint

for i in range(6):
    for j in range(36):
        cprint(' ', 'red', 'on_red', end='')
    print()

for i in range(6):
    for j in range(36):
        cprint(' ', 'white', 'on_white', end='')
    print()
