### Task statement
Given two numbers `a` and `b` (in decimal numerical system) find `a / b` written in numerical system with base `k`. If the fraction is infinite, period should be bracketed.

**Input example:**
```
1 2 8
1 12 10
```

**Output example:**
```
0.4
0.08(3)
```

### Usage
`numsystem.py` implements `MultibaseRational` class for numerical system conversions.
You can use provided `num_system_demo()` function or run `numsystem.py` to try it.

The demo program reads three integers from keyboard and prints results.
Denominator (`b`) must be non-zero and system base must be greater than 1.

### Example
```
python numsystem.py
Enter numerator, denominator and numerical system base: 10 3 5
10 / 3 in base 5 system is 3.(13)
```
