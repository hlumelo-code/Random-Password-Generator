# this file is only for testing out specific stuff I am trying to understand.

from passwordgenerator import checkInput

def testInput():

	assert checkInput("12") == True
	assert checkInput("19967673") == True
	assert checkInput("5545g") == False
	assert checkInput("2333445450")

