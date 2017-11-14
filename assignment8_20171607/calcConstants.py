from keypad2 import constantList

def concalc(key):
    try:
        if key == constantList[0]:
            r = '3.141592'
            return r
        elif key == constantList[1]:
            r = '3E+8'
            return r
        elif key == constantList[2]:
            r = '340'
            return r
        elif key == constantList[3]:
            r = '1.5E+8'
            return r
    except:
        r = 'Error!'
        return r
