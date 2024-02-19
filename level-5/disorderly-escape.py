# DISCLAIMER: The code is copied VERBATIM from this excellent answer by Kody Puebla:
# https://math.stackexchange.com/a/2835508/377831
#
# I decided that it's not worth the time trying to grind my way through
# trying to understand Group Theory :D Though, the answer above provides 
# such an intuitively comprehensible understanding of this problem.

from math import factorial
from fractions import gcd
from fractions import Fraction

def solution(w, h, s):
    total = 0 # initialize return value
    # generate cycle indices for the set of rows and set of columns
    cycidx_cols = cycle_index(w)
    cycidx_rows = cycle_index(h)
    # combine every possible pair of row and column permutations
    for col_coeff, col_cycle in cycidx_cols:
        for row_coeff, row_cycle in cycidx_rows:
            coeff = col_coeff * row_coeff # combine coefficients
            cycle = combine(col_cycle, row_cycle) # combine cycles
            # substitute each variable for s
            value = 1
            for x, power in cycle:
                value *= s ** power
            # multiply by the coefficient and add to the total
            total += coeff * value
    return str(total)

## combines sets of variables with their coefficients to generate a complete cycle index
## returns [ ( Fraction:{coeff}, [ ( int:{length}, int:{frequency} ):{cycle}, ... ]:{cycles} ):{term}, ... ]
def cycle_index(n):
    return [(coeff(term), term) for term in gen_vars(n, n)]

## calculates the coefficient of a term based on values associated with its variable(s)
## this is based off part of the general formula for finding the cycle index of a symmetric group
def coeff(term):
    val = 1
    for x, y in term:
        val *= factorial(y) * x ** y
    return Fraction(1, val)

## generates the solution set to the problem: what are all combinations of numbers <= n that sum to n?
## this corresponds to the set of variables in each term of the cycle index of symmetric group S_n
def gen_vars(n, lim):
    soln_set = [] # store the solution set in a list
    if n > 0: # breaks recursive loop when false and returns an empty list
        for x in range(lim, 0, -1): # work backwards from the limit
            if x == 1: # breaks recursive loop when true and returns a populated list
                soln_set.append([(1, n)])
            else: # otherwise, enter recursion based on how many x go into n
                for y in range(int(n / x), 0, -1):
                    # use recursion on the remainder across all values smaller than x
                    recurse = gen_vars(n - x * y, x - 1)
                    # if recursion comes up empty, add the value by itself to the solution set
                    if len(recurse) == 0:
                        soln_set.append([(x, y)])
                    # otherwise, append the current value to each solution and add that to the solution set
                    for soln in recurse:
                        soln_set.append([(x, y)] + soln)
    return soln_set # return the list of solutions

## combines two terms of a cycle index of the form [ ( int:{length}, int:{frequency} ):{cycle}, ... ]
def combine(term_a, term_b):
    combined = []
    # combine all possible pairs of variables
    for len_a, freq_a in term_a:
        for len_b, freq_b in term_b:
            # new subscript = lcm(len_a, len_b)
            # new superscript = len_a * freq_a * len_b * freq_b / lcm(len_a, len_b)
            lcm = len_a * len_b / gcd(len_a, len_b)
            combined.append((lcm, int(len_a * freq_a * len_b * freq_b / lcm)))
    return combined


print(solution(2, 2, 2))