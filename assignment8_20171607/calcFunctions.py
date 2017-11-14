from math import factorial as fact
from keypad2 import functionList, operatorList

def funcalc(key, numStr):
    try:
        if(key == functionList[0]):
            n = int(numStr)
            r = str(fact(n))
            return r
        elif(key == functionList[1]):
            n = int(numStr)
            r = bin(n)[2:]
            return r
        elif(key == functionList[2]):
            n = int(numStr)
            r = bin(n)[2:]
            return r
        else:
            return 'dec -> Roman'
    except:
        r = 'Error!'





