def fibo(n):
	
	if n == 0: 
		print("Calculating fibo via " + str(n))
		return 0
	if n == 1: 
		print("Calculating fibo via " + str(n))
		return 1
	print("Calculating fibo(" + str(n) + ") via fibo(" + str(n - 1) + ") and fibo(" + str(n - 2) + ")")
	return fibo(n - 1) + fibo(n - 2)

print("Final answer: " + str(fibo(10)))