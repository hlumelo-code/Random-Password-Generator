#!/usr/bin/env python3

import random
import string
		
def pwgen(): # this function will generate the string with random characters.

	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
	i = 0
	word = ""
	while i < 13:
		word = word + random.choice(chars)
		i = i + 1
	return word
