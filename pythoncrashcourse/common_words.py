filename='little_prin.txt'
try:
	with open(filename) as file:
		contents=file.read()
except FileNotFoundError:
	print('File not found.')
else:
	count=contents.lower().count('the')
	print(count)
