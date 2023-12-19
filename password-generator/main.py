from termcolor import colored, cprint
from password.generate_password import Password

# Main
if __name__ == "__main__":
	length = int(input("Enter the number of characters b/w 8-32 characters:\n"))
	obj = Password(length)

	password = obj.generate_password()

	print(f'Generated Password :: {password}')

	result = obj.check_strength(password)

	if result == "Strong Password":
		final_result = colored(result,'green', attrs=['reverse', 'blink'])
	else:
		final_result = colored(result,'yellow', attrs=['reverse', 'blink'])

	print(f'Strength :: {final_result}')