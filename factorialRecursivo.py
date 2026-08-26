import time
def factorial(n):
	if n==0 or n==1:
		return 1
	return n * factorial(n-1)
inicio = time.time()
print(factorial(100))
fin = time.time()
print(fin-inicio)

	