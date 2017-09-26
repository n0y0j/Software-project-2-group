

def Combination(s,t):
    if s==t :
        return 1
    elif t == 0 :
        return 1
    elif t<0:
        return 0
    return Combination(s-1,t-1) + Combination(s-1, t)

    

while True:
    try:
        n = int(input("Enter n: "))
        if n<0 :
            break
        elif n>0:
            m = int(input("Enter m: "))
            print("C(%d,%d) = %d" % (n, m, Combination(n, m)))
    except (RecursionError,ValueError):
        print("입력된 수가 올바르지 않습니다. 다시 입력해주세요")