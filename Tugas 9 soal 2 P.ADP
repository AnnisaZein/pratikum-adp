from termcolor import colored, cprint

for i in range(9):
	for j in range(25-i*3-1):
		cprint(' ', 'black', 'on_black', end='')
	for j in range(i * 6 + 4):
		cprint(' ', 'red', 'on_red', end='')
	print()
	
for i in range(3):
	for j in range(1):
		cprint(' ','black', 'on_black',end='')
	for j in range(50):
		cprint(' ', 'white', 'on_white', end='')
	print()
	

for i in range(6):
	for j in range(1):
		cprint(' ','black', 'on_black',end='')
	for j in range(20):
		cprint(' ', 'white', 'on_white', end='')
	for j in range(10):
		cprint(' ', 'blue', 'on_blue', end='')
	for j in range(20):
		cprint(' ', 'white', 'on_white', end='')
	print()

for i in range(1):
	for j in range(52):
		cprint(' ', 'cyan', 'on_cyan', end='')
	print()





