import time
def factorial(n):
    factor = 1
    for i in range(1, n+1):
        factor = factor * i
    return factor
inicio = time.time()
print(factorial(1000))
fin= time.time()
print(fin-inicio)

