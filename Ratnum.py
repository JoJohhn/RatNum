
class RatNum:
    def __init__(self, num_m, num_n):
        if type(num_m) != int:
            raise TypeError('m must be type <int>')
        elif type(num_n) != int:
            raise TypeError('n must be type <int>')
        elif num_n < 0:
            raise ValueError('n should not be less than zero')
        else:
            self.rational_number = (num_m, num_n)

    def is_nan(self):
        if self.rational_number[1] == 0:
            return True
        else:
            return False

    def is_negative(self):
        if self.rational_number[0] < 0 and not self.is_nan():
            return True
        else:
            return False

    def is_positive(self):
        if self.rational_number[0] >= 0 and not self.is_nan():
            return True
        else:
            return False

    def __add__(self, other):
        num_m = (self.rational_number[0] * other.rational_number[1]) + \
                (other.rational_number[0] * self.rational_number[1])
        num_n = self.rational_number[1] * other.rational_number[1]
        return RatNum(num_m, num_n)

    def __sub__(self, other):
        num_m = (self.rational_number[0] * other.rational_number[1]) - \
                (other.rational_number[0] * self.rational_number[1])
        num_n = self.rational_number[1] * other.rational_number[1]
        return RatNum(num_m, num_n)

    def __mul__(self, other):
        num_m = self.rational_number[0] * other.rational_number[0]
        num_n = self.rational_number[1] * other.rational_number[1]
        return RatNum(num_m, num_n)

    def __truediv__(self, other):
        if self.is_nan() or other.is_nan():
            return RatNum(0, 0)
        else:
            return self * RatNum(other.rational_number[1], other.rational_number[0])

    def __str__(self):
        if self.is_nan():
            return 'NaN'
        elif self.rational_number[0] % self.rational_number[1] == 0:
            return str(self.rational_number[0] // self.rational_number[1])
        else:
            return f'{self.rational_number[0]}/{self.rational_number[1]}'


if __name__ == '__main__':



    listM = ['Test', 32.532, [42, 54], 'NaN']
    for m in listM:
        try:
            RatNum(m, 23)
        except TypeError:
            print(f'Test passed: m = {m}')
        else:
            print(f'Test failed: m = {m}')

    listN = ['Test', 23146.5432, [42, 54], 'NaN']
    for n in listN:
        try:
            RatNum(10, n)
        except TypeError:
            print(f'Test passed: n = {n}')
        else:
            print(f'Test failed: n = {n}')

    n = -22
    try:
        RatNum(10, n)
    except ValueError:
        print(f'Test passed: n = {n}')
    else:
        print(f'Test failed: n = {n}')

    print(RatNum(2, 0))
    print(RatNum(2, 0).is_nan())
    print(RatNum(-2, 0).is_negative())
    print(RatNum(0, 2))
    print(RatNum(0, 2).is_nan())
    print(RatNum(-2, 2).is_negative())
    print(RatNum(14, 2))

    s1 = RatNum(-2, 4)
    s2 = RatNum(-1, 2)
    s3 = s1 + s2
    print(s3)

    s4 = RatNum(1, 2)
    s5 = RatNum(1, 2)
    s6 = s4 - s5
    print(s6)

    s7 = RatNum(1, 2)
    s8 = RatNum(1, 10)
    s9 = s7 / s8
    print(s9)