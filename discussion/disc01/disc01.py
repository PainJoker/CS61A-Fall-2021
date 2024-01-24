def wears_jacket_with_if(temp, raining):
    """Q1.1 Using if statement to solve whether Alfonso wear a jacket.
    Alfonso will only wear a jacket outside if it is below 60 degree or it is raining. 

    Args:
        temp (int): outside temperature
        raining (bool): True for raining
    
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    # if temp < 60 or raining:
    #     return True
    # else:
    #     return False
    
    # Notice that return value is based on the single if condition
    # We could condense it into one single statement below
    return temp < 60 or raining

    
def is_prime(n):
    """
    Q1.3 
    
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """ 
    assert n > 0, "argument must be positive."
    if n == 1:
        return False
    k = 2
    while k < n // 2:
        if n % k == 0:
            return False
        k += 1
    return True 
    