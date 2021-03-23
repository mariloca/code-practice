
print("Enter 'q' to quit.")
while True:
	number1=input("Enter the first number: ")
	if number1=='q':
		break
	number2=input("Enter the second number: ")
	if number2=='q':
		break
	try:
		result=int(number1)+int(number2)
	except ValueError:
		pass
	else:
		print(result)



