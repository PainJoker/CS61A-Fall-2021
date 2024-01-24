"""Practice for higher order function"""
from math import sqrt 
# 1.6.1 Functions as Arguments
def identity(k):
    return k

def cube(k):
    return k**3

def summation(n, term):
    """Sum the first N term of natural numbers.

    Args:
        n (int): number of summation term
        term (func): function of natural number
        
    >>> summation(5, identity)
    15
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1

def sum_naturals(n):
    """Sum the first N natural numbers.
    
    >>> sum_naturals(5)
    15
    """
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)
        
# 1.6.2 Functions as General Method
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def phi_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

phi = (sqrt(5)+1) / 2
phi_approx = improve(phi_update, square_close_to_successor)
assert abs(phi - phi_approx) < 1e-15, "Golden ratio approximation is not precise."

# 1.6.3 Defining Function Ⅲ: Nested Definition
def average(x, y):
    return (x+y) / 2

# The update func need 2 args instead of 1 for improve func
# ( We can use nested func to get one argument "fixed" )
# Notice: the idea shown above slightly differs from this example
# closure versus currying
# Maybe just two sides of a coin?
# def sqrt_update(x, a):
#     return average(x, a/x)

def sqrt(a):
    """Return square root of "a"

    Args:
        a (double): any positive number
    
    >>> sqrt(64)
    8
    >>> sqrt(9)
    3
    """
    def sqrt_update(x):
        return average(x, a/x)
    
    def sqrt_close(x):
        return approx_eq(x*x, a)
    
    return improve(sqrt_update, sqrt_close)

# sqrt_update enclose the info of value a --> "closure"
# It is in a kind of multi variable func field?

# 1.6.4 Functions as Return Values
def compose(f, g):
    # Alternative lambda form:
    # return lambda x: f(g(x))
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x 

def square(x):
    return x * x    

squriple = compose(square, triple)
triquare = compose(triple, square)

# Example: Self-reference
def print_all(x):
    print(x)
    return print_all

def print_sum(x):
    print(x)
    def print_next(y):
        return print_sum(x+y)
    return print_next

# 1.6.5 Example: Newton's Method
# It does not always converge
def newton_update(f, df):
    # Alternative lambda form:
    # return lambda x: x - f(x)/df(x)
    def update(x):
        return x - f(x)/df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    
    return improve(newton_update(f, df), near_zero)

def nth_root_of_a(n, a):
    def f(x):
        return pow(x, n) - a
    def df(x):
        return n*pow(x, n-1)
    return find_zero(f, df) 

# 1.6.6 Currying
# Currying is useful when we require a function that takes in only a single argument.
def curried_pow(x):
    def g(y):
        return pow(x, y)
    return g

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1

def curry2(f):
    """Return a curried version of the given 2-argument input func."""
    # Alternative form:
    # return lambda x, y: f(x, y) 
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """Return a inverse of curried 2-argument func."""
    def f(x, y):
        return g(x)(y)
    return f

# 1.6.9 Function Decorators
def trace(fn):
    def wrapped(x):
        print(f"--> {fn}({x})")
        return fn(x)
    return wrapped

@trace
def decorator_test(x):
    return 3 * x

# the decorator def statement is equivalence to
# decorator_test = trace(decorator_test)
