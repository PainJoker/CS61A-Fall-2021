def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    times_to_add = list(filter(lambda el: el == x, s))
    for _ in times_to_add:
        s.append(el)


def filter_iter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for item in iterable:
        if fn(item):
            yield item
        
        
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    item_a, item_b = next(a), next(b)
    pregen = []
    while True:
        if item_a > item_b:
            if item_b not in pregen:
                pregen.append(item_b)
                yield item_b
            item_b = next(b)
        else:
            if item_a not in pregen:
                pregen.append(item_a)
                yield item_a
            item_a = next(a)

            
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n < 2:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)


def primes_gen_ascending(n):
    """Generates primes in ascending order.
    >>> pg = primes_gen_ascending(7)
    >>> list(pg)
    [2, 3, 5, 7]
    """
    def prime_gen(i):
        if i > n:
            return 
        if is_prime(i):
            yield i
        yield from prime_gen(i + 1)
    yield from prime_gen(2)


def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)