import random

value = random.randint(1, 100)
count = 0

while 1:
	vinput = int(input("Number: "))
	if   value < vinput:
		print("Your value is too big.")
		count += 1
	elif value > vinput:
		print("Your value is too low.")
		count += 1
	else:
		print("You won, the number was "+str(value)+" and you did "+str(count)+" mistakes.")
		break
		
input()