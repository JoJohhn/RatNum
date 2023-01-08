
class RatNum:
    def __init__(self, num_m, num_n):
        if type(num_m) != int:
            raise TypeError('m must be type <int>')
        elif type(num_n) != int:
            raise TypeError('n must be type <int>')
        elif num_n < 0:
            raise ValueError('n should not be less than zero')
        elif num_n == 0:
            self.rational_number = 'NaN'
        elif num_m == 0:
            self.rational_number = 0
        else:
            self.rational_number = (num_m, num_n)

    def __str__(self):
        if self.rational_number == 'NaN':
            return 'NaN'
        elif self.rational_number == 0:
            return '0'
        else:
            return f'({self.rational_number[0]}/{self.rational_number[1]})'


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
    print(RatNum(0, 2))
