import random
from termcolor import colored, cprint
import sys
import secrets

class Password:
	def __init__(self,password_len=8):
		self.password_len = password_len
		self.char_list = self._get_char_list()

	def _get_char_list(self):
		uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		lowercase_letters = "abcdefghijklmnopqrstuvwxyxz"
		digits = "012345678910"
		special_characters = "!#@$%^&_*()[]/|-"

		return uppercase_letters + lowercase_letters + digits + special_characters

	def generate_password(self):
		error = colored('Invalid length!!Please try again!!','red', attrs=['reverse','blink'])
		if self.password_len < 8:
			print(error)
			sys.exit(0)
		else:
			password = ''.join(secrets.choice(self.char_list) for _ in range(self.password_len))
			return password

	def check_strength(self,password):
		# Password should contain at least 8 characters
		min_len = 8

		# Password must have at least one uppecase letter.
		has_uppercase = any(char.isupper() for char in password)

		# Password must have at least one lowercase letter.
		has_lowercase = any(char.islower() for char in password)

		# Password must have at least one digit.
		has_digit = any(char.isdigit() for char in password)

		# Password must have at least one special character.
		special_characters = ["@","#","!","$","^","%","*","(",")","/","|","[","]","_","-","&"]
		has_special = any(char in special_characters for char in password)

		if len(password) >= min_len and has_uppercase and has_lowercase and has_special and has_digit:
			return "Strong Password"
		else:
			return "Weak Password"

# Main
# if __name__ == "__main__":
# 	length = int(input("Enter the number of characters b/w 8-32 characters:\n"))
# 	obj = Password(length)

# 	password = obj.generate_password()

# 	print(f'Generated Password :: {password}')

# 	result = obj.check_strength(password)

# 	if result == "Strong Password":
# 		final_result = colored(result,'green', attrs=['reverse', 'blink'])
# 	else:
# 		final_result = colored(result,'yellow', attrs=['reverse', 'blink'])

# 	print(f'Strength :: {final_result}')