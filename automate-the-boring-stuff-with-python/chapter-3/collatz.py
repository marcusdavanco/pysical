import sys

def collatz(number):
	if number % 2 == 0:
		return number // 2
	else: 
		return number * 3 +  1

while True:
	try:
		selectedNumber = input('Type a number \n')
		print(collatz(int(selectedNumber)))
	except ValueError:
		print('It must be a number \n')

