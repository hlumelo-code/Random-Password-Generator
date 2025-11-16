#!/usr/bin/env python3

import random
import string

def getInput():

	try:
		userInput = int(input("Enter the length of password to be generated (between 8 and 15): "))
		if (userInput < 8 or userInput > 15):
			print("please enter a length between 7 and 15\n")
			return -1
		else:
			return userInput
	except ValueError:
		print("Invalid input.")
		return -1
		
def pwgen(userInput): # this function will generate the string with random characters.

	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	i = 0
	word = ""
	while i < userInput:
		word = word + random.choice(chars)
		i = i + 1
	return word

def passwordgenerator():

	try:
		userInput = getInput()
		if userInput == -1:
			passwordgenerator()
		else:
			print("Your generated password is",pwgen(userInput))
	except KeyboardInterrupt:
		print("\nYou exited the program before the password was generated. Try again.")
