
# Returns the absolute value of a number

def abs(n):
    if not (isinstance(n, int) or isinstance(n, float)):
        raise ValueError("Not a Number")
    
    if n < 0:
        return -n
    else:
        return n