#!/usr/bin/env python3

import random

def getInput():

	userInput = ""
	userInput = userInput + input("Please enter the length of password to generate \n")
	return userInput

def checkInput(user_input): # this function will check if all the characters in string input are numeric.
	
	if (user_input.isnumeric()==True):
		return True
	return False

def pwgen(number): # this function will generate the string with random characters.

	chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
	i = 0
	word = ""
	while i < number:
		pos = random.randint(0,61)
		word = word + chars[pos]
		i = i + 1
	return word

def main():

	user_input = getInput()
	eval_input = checkInput(user_input)

	if eval_input == True:
		print("Your generated password is",pwgen(int(user_input)))
	else:
		print("invalid input")
		main()

if __name__ == '__main__':
	main()