from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        if a >= b:
            raise ValueError("For a proper fraction, numerator must be less than denominator.")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        """Simplify the fraction to its lowest terms."""
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.a * other.b + other.a * self.b
            new_denominator = self.b * other.b
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.a * other.b - other.a * self.b
            new_denominator = self.b * other.b
            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a
        return NotImplemented

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
