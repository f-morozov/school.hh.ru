### Task statement
You are given an expression containing brackets, addition, subtraction, multiplication and constant power operations and one variable e. g. `(x - 5)(2x^3 + x(x^2 - 9))`.
Represent this expression in expanded form e. g. `3x^4 - 15x^3 - 9x^2 + 45x`.

### Description
`parser.py` implements `Parser` class for expression parsing.
You can use provided `parser_demo()` function or run `parser.py` to try it.
The demo program reads expression from keyboard and prints the resulting polynom.

Parser supports expressions with integers and one variable name containing only letters.
Supported operations are `+`, `-`, `*`, `^`, unary `-` and brackets. Implicit multiplication is assumed when possible. 

All operations are evaluated from left to right except `^`. All expressions used as powers should evaluate to constants.
Spaces are ignored outside variable names so `1 000` is `1000` but `x x` is `x^2`.

Approximate grammar looks like this:

```
expr = sum
sum = mul (+|- mul)*
mul = unary (pow | * unary)* # Implicit multiplication can't be followed by unary minus
unary = -* pow
pow = item (^item)* # All powers should evaluate to constants
item = ( expr ) | const | var
const = (0-9)+
var = (a-z | A-Z)+
```

### Examples
```
> python parser.py
Enter expression: (x+1)(x-1)*2
2x^2 - 2
```

```
> python parser.py
Enter expression: -hh * (hh + 2)(hh-1)^2^3
-hh^10 + 6hh^9 - 12hh^8 + 42hh^6 - 84hh^5 + 84hh^4 - 48hh^3 + 15hh^2 - 2hh
```
