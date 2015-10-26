import string

class MultibaseRational:
    """Rational number that can be represented in given numerical system
    :param int num: numerator
    :param int ratio: denomenator
    :param int base: numerical system to represent in (default None)
    """
    def __init__(self, num, ratio, base = None):
        if not ratio:
            raise ValueError("Denominator can't be 0")       
        self._sign = -1 if num / ratio < 0 else 1
        self._num = abs(num)
        self._ratio = abs(ratio)
        if base is not None:
            self.to_num_system(base)

    def to_num_system(self, base):
        """Converts stored number to given numerical system
        :param int base: numerical system base
        """
        if base < 2:
            raise ValueError("Numerical system base can't be less than 2")
        self._base = base
        self._calc_integral()
        self._calc_fractional()

        alphabet = string.digits + string.ascii_uppercase
        if base <= len(alphabet):
            self.alphabet = list(alphabet)[:base]
        else:
            self.alphabet = list(string.digits)
            self.alphabet.extend(map('[{0}]'.format, range(10, self._base)))

    def _calc_integral(self):
        """Calculate integral part of the number"""
        num = self._num // self._ratio
        self._integral = []
        while num:
            num, mod = divmod(num, self._base)
            self._integral.append(mod)
        self._integral.reverse()

    def _calc_fractional(self):
        """Calculate fractional part and period of the number """
        num = self._num % self._ratio
        self._fractional = []
        self._period = []
        used = {}
        while num:
            used[num] = len(self._fractional)
            digit, num = divmod(num * self._base, self._ratio)
            self._fractional.append(digit)
            if num in used.keys():
                self._period = self._fractional[used[num]:]
                self._fractional = self._fractional[:used[num]]
                break

    def __str__(self):
        """Convert fraction to string. Digits and letters are used as digits.
        If they are not enough then [digit] notation is used for digits > 9.
        Examples:
        if base = 8 digits are 0-7
        if base = 16 digits are 0-9, A-F
        if base = 100 digits are 0-9, [10], [11] ... [99]
        """
        def to_str(digits):
            return ''.join(self.alphabet[x] for x in digits)

        res = '-' if self._sign < 0 else ''
        res += to_str(self._integral) if self._integral else self.alphabet[0]
        if self._fractional or self._period:
            res += '.'
        res += to_str(self._fractional)
        if self._period:
            res += '(' + to_str(self._period) + ')'
        return res


def num_system_demo():
    """Read fraction and base from keyboard and print the results"""
    try:
        input_str = input('Enter numerator, denominator '
                          'and numerical system base: ')
        num, ratio, base = map(int, input_str.split())
        res = MultibaseRational(num, ratio, base)
        formatStr = '{0} / {1} in base {2} system is {3}'
        print(formatStr.format(num, ratio, base, res))
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    num_system_demo()    