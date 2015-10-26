from polynom import Polynom

class ParseError(Exception):
    """Exception class for all parser errors
    :param str expr: expression with error
    :param int pos: error position
    :param str error: error description
    """
    def __init__(self, expr, pos, error):
        self._pos = pos
        self.error = error
        self._expr = expr

    def __str__(self):
        """Return str with expr highlighting error position"""
        return '\n'.join((self._expr,
                          ' ' * self._pos + '^',
                          '{0}: {1}'.format(self._pos, self.error)))

class Parser:
    """Parser for polynom expressions with one variable"""

    def parse_expr(self, expr):
        """Parse expression. If it's incorrect raise ParseError.
        :param str expr: expression to parse
        :return: resulting polynom
        """
        self._expr = expr
        self._pos = 0
        self.var_name = None
        res = self._parse_sum()
        if self._pos != len(self._expr):
            self._raise_error("Unrecognized symbol")
        return res

    def _skipspace(self):
        while (self._pos < len(self._expr) and self._cur().isspace()):
            self._pos += 1

    def _step(self, skipspace = True):
        """Proceed to next symbol"""
        if self._pos < len(self._expr):
            self._pos += 1
        if skipspace:
            self._skipspace()

    def _cur(self):
        """Return current symbol"""
        if self._pos < len(self._expr):
            return self._expr[self._pos]
        else:
            return '\0'

    def print_expr(self, expr):
        """Parse and the print expression"""
        res = self.parse_expr(expr)
        if res:
            print(res.to_string(self.var_name))

    def _raise_error(self, error):
        raise ParseError(self._expr, self._pos, error)

    def _parse_sum(self):
        """Gradient descent step parsing + and - operators"""
        res = self._parse_mult()
        if not res:
            return None
        while self._cur() in '+-':
            sign = self._cur()
            self._step()

            mult = self._parse_mult()
            if not mult:
                self._raise_error("Expected expression")
            if sign == '+':
                res += mult
            else:
                res -= mult
        return res

    def _parse_mult(self):
        """Gradient descent step parsing explicit and implicit * operator"""
        res = self._parse_minus()
        if not res:
            return None
        while True:
            if self._cur() == '*':
                self._step()
                term = self._parse_minus()
                if not term:
                    self._raise_error("Expected expression")
            else:
                term = self._parse_power()
                if not term:
                    break
            res *= term
        return res

    def _parse_minus(self):
        """Gradient descent step parsing unary -"""
        sign = 1
        needExpr = (self._cur() == '-')
        while self._cur() == '-':
            self._step()
            sign = -sign
        term = self._parse_power()
        if needExpr and not term:
            self._raise_error("Expected expression")
        return term if sign > 0 else -term

    def _parse_power(self):
        """Gradient descent step parsing ^ operator"""
        res = self._parse_item()
        if not res:
            return None
        powers = []
        while self._cur() == '^':
            self._step()
            val = self._parse_item()
            if not val:
                self._raise_error("Expected exprssion")
            powers.append(val)
        if not powers:
            return res
        try:
            for i in range(len(powers) - 1, 0, -1):
                powers[i - 1] **= powers[i]
            return res ** powers[0]
        except ValueError as error:
            self._raise_error(error)

    def _parse_item(self):
        """Gradient descent step detecting brackets, variables and constants"""
        if self._cur() == '(':
            self._step()
            res = self._parse_sum()
            if not res:
                self._raise_error("Expected Expression")
            if self._cur() != ')':
                self._raise_error("Expected )")
            self._step()
            return res
        elif self._cur().isalpha():
            return self._parse_name()
        elif self._cur().isdigit():
            return self._parse_const()
        else:
            return None
        
    def _parse_const(self):
        """Gradient descent step parsing integer constants"""
        res = ""
        while self._cur().isdigit():
            res += self._cur()
            self._step()
        return None if not res else Polynom({0:int(res)})

    def _parse_name(self):
        """Gradient descent step parsing variable names"""
        name = ""
        while self._cur().isalpha():
            name += self._cur()
            self._step(skipspace=False)         
        self._skipspace()   
        if not name:
            return None
        if not self.var_name:
            self.var_name = name
        if self.var_name != name:
            self._raise_error("Only one variable is supported")
        return Polynom({1:1})


def parser_demo():
    """Read expression from keyboard and print simplified polynom"""
    expr = input("Enter expression: ")
    try:
        Parser().print_expr(expr)
    except (ParseError, RecursionError) as error:
        print(error)


if __name__ == "__main__":
    parser_demo()