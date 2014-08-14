def fibo(n):
	if n == 0 or n == 1:
		return n
	a = 1 # f(n-2)
	b = 1 # f(n-1)
	ret = 0
	for x in range(2, n):
		ret = a + b
		a = b
		b = ret
	return ret
	
def fibo_rec(n):
	if n == 0: return 0
	if n == 1: return 1
	return fibo(n - 1) + fibo(n - 2)

import time

def compare_functions(f, g, arg):
  i = 0
  t1 = 0
  t2 = 0
  while i < 1000:
    last_time = time.clock()
    f(arg)
    t1 += time.clock() - last_time
    last_time = time.clock()
    g(arg)
    t2 += time.clock() - last_time
    i += 1
  print(t2 / t1)
  
compare_functions(fibo, fibo_rec, 410)