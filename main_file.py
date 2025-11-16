# the idea is to use this file for communicating with the user
# while the passwordgenerator file generates the password if the
# user chooses to auto-create it, and will have the option to 
# generate it themselves. length rule still apllies to both.

from passwordgenerator import start
from passwordgenerator import evalCreated

def main():

    try: 
        password = ""
        decide = input("Do you want to \n1. create your own password or \n2. generate a random password?\n 1 or 2:  ")
        if decide == "1":
            password = input("\nPlease enter your new password: ")
            if evalCreated(password) == False:
                print("\nPlease make you password be 8 to 15 characters\n")
                main()
        elif decide == "2":
            password = start()
            print("Your randomly generated password is",password)
        else:
            print("invalid input")
    except KeyboardInterrupt:
        print("\nYou close the program unexpectedly. Try again")

if __name__ == '__main__':
	main()