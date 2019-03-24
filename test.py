usr_input = 0
val1 = input("Enter First Value: ")
while not val1.isdigit():
	print("Enter Number Only")
	val1 = input("Enter First Value: ")
val1 = int(val1)
val2 = input("Enter Second value: ")
while not val2.isdigit():
	print("Enter number only")
	val2 = input("Enter Second Value: ")
val2 = int(val2)
def sumofnum(*args):
	result = val1 + val2
	print(result)

def subofnum(*args):
	result = val1 - val2
	print(result)

def mulofnum(*args):
	result = val1 * val2
	print(result)

def divofnum(*args):
	result = val1 / val2
	print(result)

while not usr_input == 5:
	print("Enter Numbers Only")
	usr_input = input("""Please Select any Option:
	1. Addition
	2. Substraction
	3. Multiply
	4. Division
	5. Exit
	""")
	while not usr_input.isdigit():
		print("Enter an integer value from option.")
		usr_input = input("Enter your choice: ")
	usr_input = int(usr_input)

	if usr_input == 1:
		sumofnum(val1,val2)
	if usr_input == 2:
		subofnum(val1,val2)
	if usr_input == 3:
		mulofnum(val1,val2)
	if usr_input == 4:
		divofnum(val1,val2)
	if usr_input == 5:
		break


