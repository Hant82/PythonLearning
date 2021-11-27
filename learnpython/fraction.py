def hcf(x, y):
    x, y = abs(x), abs(y)
    hcf = x if x < y else y

    while hcf > 0:
        if x % hcf == 0 and y % hcf == 0:
            break
        hcf -= 1
        if hcf > 0:
            return hcf
        else:
             None
class Fraction:
    def __init__(self, nr, dr=1):
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải khác 0")

        if dr < 0:
            self.nr = nr * -1
            self.dr = dr * -1
        else:
            self.nr = nr
            self.dr = dr

        self._reduce()

    def __repr__(self):
        
        if self.nr == 0:
            return "0"
        if self.dr == 1:
            return str(self.nr)
        else:
            return f"{self.nr}/{self.dr}"


    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) + (other.nr * self.dr), self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)

    def _reduce(self):
        usc = hcf(self.nr, self.dr)

        if usc:
            self.nr = int(self.nr / usc)
            self.dr = int(self.dr / usc)


fr = Fraction(0, 2)
other = Fraction(1.5, 1)
print(fr, other)

print()

print(fr + other)
print(fr - other)
print(fr * other)
print(fr / other)

print()

fr = Fraction(1, 2)
print(fr + 1)
print(fr - 1.5)
print(fr * 2)
print(fr / 2)
