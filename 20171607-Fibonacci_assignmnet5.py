import time

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    if n<=1:
        return n
    else:
        sum = 0
        list = [0, 1]
        for i in range(1, n-1):
            list.append(list[i-1] + list[i])
        sum = list[n-1] + list[n-2]
        return sum


while True:
    nbr = int(input("Enter a number : "))
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
