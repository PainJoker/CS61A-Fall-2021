def sum_recur(L):
    """Return the sum of a list by recursion.

    >>> sum_recur([1, 2, 3, 4])
    10
    >>> sum_recur([])
    0
    """
    if L == []:
        return 0
    else:
        return L[0] + sum_recur(L[1:])

def sum_iter(L):
    """Return the sum of a list by iteration.

    >>> sum_iter([1, 2, 3, 4])
    10
    >>> sum_iter([])
    0
    """
    total = 0
    for item in L:
        total += item
    return total
    
def recur_sum_until(n):
    """Return the sum of integers from 0 until n using recursion.

    Args:
        n (int): n >= 0
    
    >>> recur_sum_until(4)
    10
    >>> recur_sum_until(0)
    0
    """
    if n == 0:
        return 0
    else:
        return n + recur_sum_until(n - 1)
    
def iter_sum_until(n):
    """Return the sum of integers from 0 until n using iteration.

    Args:
        n (int): n >= 0
    
    >>> iter_sum_until(4)
    10
    >>> iter_sum_until(0)
    0
    """
    total, i = 0, 0
    while i <= n:
        total, i = total + i, i + 1
    return total

def reverse_recur(s):
    """Return a reverse version of string s using recursion.

    >>> reverse_recur('abc')
    'cba'
    >>> reverse_recur('a')
    'a'
    >>> reverse_recur('')
    ''
    """
    if s == "":
        return s
    else:
        return reverse_recur(s[1:]) + s[0]