#!/usr/bin/env python3

import random

def getInput():

	try:
		userInput = input("Please enter the length of your password\n")
		return int(userInput)
		
	except ValueError:
		print("Invalid input")
		

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

	print("Your generated password is",pwgen(userInput))

if __name__ == '__main__':
	main()