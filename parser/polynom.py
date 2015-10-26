class Polynom:
    """Polynom stores dict with power and non-zero coefficient pairs.
    Supports basic arithmetic operators and constant power operator.
    :param coeff: initial coefficients (default None)
    """
    def __init__(self, coeff = None):
        self.coeff = {}
        if coeff is None:
            return 
        for i in coeff:
            if coeff[i]:
                self.coeff[i] = coeff[i]

    def __iadd__(self, other):
        for i in other.coeff:
            self.coeff.setdefault(i, 0)
            self.coeff[i] += other.coeff[i]
            if not self.coeff[i]:
                self.coeff.pop(i)
        return self

    def __isub__(self, other):
        self += -other
        return self

    def __add__(self, other):
        res = Polynom()
        res += self
        res += other
        return res

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        for i in self.coeff:
            self.coeff[i] = -self.coeff[i]
        return self

    def __mul__(self, other):
        res = Polynom()
        for i in self.coeff:
            for j in other.coeff:
                val = self.coeff[i] * other.coeff[j]
                res += Polynom({i + j : val})
        return res

    def __pow__(self, power):
        if power.coeff and list(power.coeff.keys()) != [0]:
            raise ValueError('Only constant powers allowed')
        res = Polynom({0:1})
        if not power.coeff:
            return res
        for i in range(power.coeff[0]):
            res *= self
        return res

    def to_string(self, varName):
        """Print polynom using given variable name"""
        if not self.coeff:
            return '0'
        strings = []
        for i in sorted(self.coeff.keys(), reverse=True):
            strings.append('+' if self.coeff[i] >= 0 else '-')
            val = ''
            if abs(self.coeff[i]) != 1 or not i:
                val += str(abs(self.coeff[i]))
            if i > 0:
                val += varName
            if i > 1:
                val += '^' + str(i)
            strings.append(val)
        sign = '-' if strings[0] == '-' else ''
        return sign + ' '.join(strings[1:])

    def __str__(self):
        """Print polynom using default variable name 'x'"""
        return self.to_string('x')
