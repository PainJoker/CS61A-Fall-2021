def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer/r.denom, c.imag)


def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)


def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)


def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)


class Number:
    adders = {("com", "rat"): add_complex_and_rational,
              ("rat", "com"): add_rational_and_complex}
    multipliers = {("com", "rat"): mul_complex_and_rational,
                   ("rat", "com"): mul_rational_and_complex}
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)
    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)
    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)


class Complex(Number):
    type_tag = "com"
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)


from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __repr__(self):
        return f"ComplexRI({self.real:g}, {self.imag:g})"
        
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    

from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    def __repr__(self):
        return f"ComplexMA({self.magnitude:g}, {self.angle/pi:g} * pi)"
    
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    
        
from math import gcd
class Rational(Number):
    type_tag = "rat"
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx*dy + ny*dx, dx*dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

        
def is_real(c):
    """Return whether c is a real number with no imaginary part."""
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0


class Kangaroo():
    """
    >>> k = Kangaroo()
    >>> print(k)
    The kangaroo's pouch is empty.
    >>> k.put_in_pouch("ball")
    >>> k.put_in_pouch("ball")
    object already in pouch.
    >>> print(k)
    The kangaroo's pouch contains: ['ball']
    >>> k.put_in_pouch("soccer")
    >>> print(k)
    The kangaroo's pouch contains: ['ball', 'soccer']
    """
    def __init__(self):
        self.pouch_contents = []
        
    def put_in_pouch(self, content):
        if content in self.pouch_contents:
            print('object already in pouch.')
        else:
            self.pouch_contents.append(content)
        
    def __str__(self):
        if len(self.pouch_contents) == 0:
            return "The kangaroo's pouch is empty."
        else:
            return f"The kangaroo's pouch contains: {self.pouch_contents}"