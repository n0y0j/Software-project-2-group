def factorial(f):
    return 1 if f == 0 else factorial(f-1)*f

def Combination(q,t,r):
    if q == t :
        return 1
    else :
        comb = q/((r)*(t))
    return comb

while True:
    try:
        n = int(input("Enter n: "))
        if n<0:
            break
        elif n>0:
            m = int(input("Enter m: "))
            j = n-m
            k = factorial(n)
            l = factorial(m)
            g = factorial(j)

            print("C(%d,%d) = %d " %(n,m,Combination(k,l,g)))
    except (RecursionError,ValueError):
        print("입력된 수가 올바르지 않습니다. 다시 입력해주세요")

