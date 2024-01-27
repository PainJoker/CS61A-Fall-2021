def multiply(m, n):
    """ Takes two positive integers and returns their product using
    recursion.
    >>> multiply(5, 3)
    15
    """
    if m == 0 or n == 0:
        return 0
    elif m == 1:
        return n
    else:
        return n + multiply(m - 1, n)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # iterative version, assume n > 1
    # i = 2
    # while i <= sqrt(n):
    #     if n % i == 0:
    #         return False
    #     i += 1
    # return True
    def factor(i):
        # base case
        if i == 1:
            return True
        # recursive case
        if n % i == 0:
            return False
        else:
            return factor(i - 1)
    return factor(n // 2)    


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    # base case
    if n == 1:
        return 1
    # recursive case
    if n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(3 * n + 1) + 1
        

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    # base case
    if n1 > 0 and n2 == 0:
        return n1
    elif n1 == 0 and n2 > 0:
        return n2
    elif n1 == 0 and n2 == 0:
        return 0
    # recursive case
    if n1 > 0 and n2 > 0:
        a1, last1 = split(n1)
        a2, last2 = split(n2)
        if last1 <= last2:
            return merge(a1, n2) * 10 + last1
        else:
            return merge(n1, a2) * 10 + last2

def split(n):
    all_but_last, last = n // 10, n % 10
    return all_but_last, last
