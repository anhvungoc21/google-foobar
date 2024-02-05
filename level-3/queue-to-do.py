def solution(start, length):
    result = 0
    skip = 0

    # Calculate the sum of each line of workers
    for line in range(length, 0, -1):
        result ^= consecutive_xor(start, start + line - 1)
        start += line + skip
        skip += 1

    return result


def consecutive_xor(start, end):
    """
    Calculates the XOR of consecutative natural numbers
    from `start` through `end`, inclusive.

    When `start` equals `end`, this function practically returns `end`.

    This is the `g` function in the proof below.
    """
    return consecutive_xor_from_one(start - 1) ^ consecutive_xor_from_one(end)


def consecutive_xor_from_one(end):
    """
    Calculates the XOR of consecutive natural numbers
    from 1 through `end`, inclusive.

    This is the `f` function in the proof below.
    """
    remainder = end % 4

    if remainder == 0:
        return end
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return end + 1
    else:
        return 0


"""
===== Rationale =====

Consider a function `f(n)` that calculates the XOR of 
consecutive natural numbers from 1 to n:

    f(n) = 1 ^ 2 ^ ... ^ n

A function `g(n, m)` which calculates the XOR of consecutive natural numbers
from n to m (inclusive) can be created from `f`, that is:

    g(n, m) = f(n - 1) ^ f(m)

The following is a proof of the formula for function `g(n, m)` from the ground up.

Firstly, we use the following theorem to abbreviate the calculation of consecutive XOR's:
   
    2n ^ (2n + 1) = 1 for any natural n     (*)

In other words, any even number XOR-ed by the next natural number will produce 1. 

We can justify this by noticing that the binary representation of any even number only differs 
from the number immediately following it by the least significant digit. For example:

    10010 (18)
  ^ 10011 (19)
    -----
    00001 (1)

A corrolary of this theorem is that:

    4n ^ (4n + 1) ^ (4n + 2) ^ (4n + 3) = 0     (**)

Because:
    4n ^ (4n + 1) ^ (4n + 2) ^ (4n + 3)
  = [4n ^ (4n + 1)] ^ [(4n + 2) ^ (4n + 3)]
  = [2(2n) ^ (2(2n) + 1) ] ^ [2(2n + 1) ^ (2(2n + 1) + 1)]
  = [         1          ] ^ [             1             ]
  = 0

Therefore, `f(n)` can be calculated by considering the four cases of `n mod 4`:

a) n mod 4 = 0      =>      f(n) = n        (Abstractly, the result of the previous group of 4 is 0)
b) n mod 4 = 1      =>      f(n) = 1        (Follows directly from (*))
c) n mod 4 = 2      =>      f(n) = n + 1    (Result of n ^ 1 from (b). n is even, so its right-most bit is 0)
d) n mod 4 = 3      =>      f(n) = 0        (Follows directly from (**))

With function `f`, we can now derive function `g`:

    g(n, m) = f(n - 1) ^ f(m)

Since XOR is commutative:

    g(n, m) = f(n - 1) ^ f(m)
            = [1 ^ 2 ^ ... ^ (n - 1)] ^ [1 ^ 2 ^ ... ^ (n - 1) ^ ... ^ m]
            = (1 ^ 1) ^ (2 ^ 2) ^ ... ^ [(n - 1) ^ (n - 1)] ^ ... ^ m
            = n ^ ... ^ m

This is exactly what `g(n, m)` is defined as.
The `solution` function will use `g(n, m)` as the core for calculating consecutive XOR's.

Source:
The gist (theorem and colloraries) was 
acquired from https://komorinfo.com/en/blog/compute-xor-of-consecutive-integers/. 
The proof was derived and written by me.
"""
