from math import factorial as fact


def factorial(numStr):
    try:
        n = int(eval(numStr))
        if n<=170:
            r = str(fact(n))
        else :
            r = 'infinite'
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(eval(numStr))
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'
