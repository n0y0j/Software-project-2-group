from math import factorial as fact
from keypad2 import functionList

def factorial(numStr):
    try:
        n = int(eval(numStr))
        r = str(fact(n))
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

def callfunction(key, n):
    if (key == functionList[0]):
        return factorial(n)
    elif (key == functionList[1]):
        return decToBin(n)
    elif (key == functionList[2]):
        return binToDec(n)
    elif (key == functionList[3]):
        return decToRoman(n)