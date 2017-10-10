import time
import random

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
        f0 = 0
        f1 = 1
        if n <= 1:
                return n
        else :
                for i in range (1,n):
                        temp=f0
                        f0=f1
                        f1=temp+f1
                return f1

while True:
        nbr = int(input("Enter a number: "))
        if nbr == -1:
                break
        ts = time.time()
        fibonumber = iterfibo(nbr)
        ts = time.time() - ts
        print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
        ts = time.time()
        fibonumber = fibo(nbr)
        ts = time.time() - ts
        print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
