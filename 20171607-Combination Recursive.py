n = int(input("Enter n : "))
m = int(input("Enter m : "))

while(n>=m>=0):

    def RecursiveSum(n):
        if n==0:
            return 1
        else:
            return RecursiveSum(n-1) * n

    print("C(%d,%d) = %d " %(n,m,RecursiveSum(n)/(RecursiveSum(m)*RecursiveSum(n-m))))
    n = int(input("Enter n : "))
    m = int(input("Enter m : "))
