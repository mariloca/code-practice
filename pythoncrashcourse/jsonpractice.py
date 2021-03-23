import json

def ask_number():
	"""Ask the favorite number"""
	number=input("What is your favorite number? ")
	filename='numbers.json'
	with open(filename,'w') as f:
		json.dump(number,f)
	return number

def get_number():
	"""Get stores the favorite number"""
	filename='numbers.json'
	try:
		with open(filename) as f:
			fav_number=json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return fav_number

def read_number():
	"""Read the favorite number from the file"""
	number=get_number()
	if number:
		print("I know your favorite number! It is "+number+ "!")
	else:
		number=ask_number()
		print("Number saved.")

read_number()


