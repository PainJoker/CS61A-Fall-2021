def cascade(n):
    """Recursion demonstration

    >>> cascade(123)
    123
    12
    1
    12
    123
    """
    print(n)
    if n > 10:
        cascade(n // 10)
        print(n)

def inverse_cascade(n):
    """Show the backward result of cascade

    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)
    
def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(lambda n: None if n < 10 else grow(n), print, n // 10)
shrink = lambda n: f_then_g(print, lambda n: None if n < 10 else shrink(n), n // 10)
# ANS in class
# grow = lambda n: f_then_g(grow, print, n // 10)
# shrink = lambda n: f_then_g(print, shrink, n // 10)

def partition(n, m):
    """Return the number of partitions of N up to size of M

    Args:
        n (int): integer need to be partition
        m (int): maximum integer to be shown in the partition, m <= n
    
    >>> partition(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0 or m <= 0:
        return 0
    else:
        return partition(n - m, min(n - m, m)) + partition(n, m - 1)
    
    