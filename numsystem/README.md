### Task statement
Given two numbers `a` and `b` (in decimal numerical system) find `a / b` written in numerical system with base `k`. 
If the fraction is infinite period should be bracketed.

### Usage
`numsystem.py` implements `MultibaseRational` class for numerical system conversions.
You can use provided `num_system_demo()` function or run `numsystem.py` to try it.

The demo program reads three integers from keyboard and prints results.
Denominator (`b`) must be non-zero and system base must be greater than 1.

### Examples
```
> python numsystem.py
Enter numerator, denominator and numerical system base: 1 2 8
1 / 2 in base 8 system is 0.4
```

```
> python numsystem.py
Enter numerator, denominator and numerical system base: 1 12 10
1 / 12 in base 10 system is 0.08(3)
```