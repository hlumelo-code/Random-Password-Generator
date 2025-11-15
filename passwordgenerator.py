#!/usr/bin/env python3

import random

def getInput():

	try:
		userInput = int(input("Enter the length of password to be generated: "))
		return userInput
	except ValueError:
		print("Invalid input.")
		return -1
		
def pwgen(userInput): # this function will generate the string with random characters.

	chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
	i = 0
	word = ""
	while i < userInput:
		pos = random.randint(0,61)
		word = word + chars[pos]
		i = i + 1
	return word

def main():

	userInput = getInput()
	if userInput == -1:
		main()
	else:
		print("Your generated password is",pwgen(userInput))

if __name__ == '__main__':
	main()