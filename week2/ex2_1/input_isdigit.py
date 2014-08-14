# @author	kot_reptiloid
#
# answer for exercise 2.1
#	http://heller.ru/course/viewtopic.php?f=7&t=24

def digitInput():
	str = input()
	if str.isdigit():
		return int(str)
	else:
		print("Wrong, try again: ")
		return getDigitInput()

print("Write number: ")
test_digitInput = digitInput()
print("digitInput result:\n -> " + str(test_digitInput))
