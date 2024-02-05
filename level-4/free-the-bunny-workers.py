from itertools import combinations

def solution(num_buns, num_required):
    bunnies = [[] for _ in range(num_buns)]

    # See proof below for the number of copies of each key
    copies_per_key = num_buns - num_required + 1
    
    # All possible SORTED combinations of `copies_per_key` bunnies
    # This is used to determine which bunnies hold which key
    key_holders = combinations(range(num_buns), copies_per_key)

    # Assign keys to each bunny
    for key, holders in enumerate(key_holders):
        for holder in holders:
            bunnies[holder].append(key)

    return bunnies

'''
========== Rationale ==========

We first want to identify several unknown variables that 
are prerequisites in the key generation and distribution algorithm:

    (1) Number of distinct keys
    (2) Number of copies of each distinct key

For the first variable, consider the following proof:

    The prompt requires any `num_required` bunnies to be able to open the door,
    but any combination of `num_required - 1` bunnies must NOT. For minimality, 
    we can assume that each `num_required - 1` combination is missing 1 key.

    We therefore have an INJECTION from all `num_required - 1` combinations,
    to all distinct keys, thus the number of distinct keys is equal to the number
    of possible combinations of `num_required - 1` bunnies chosen from `num_bunnies` bunnies.
    That is:

        `num_buns` CHOOSE `num_required - 1`
        
    distinct keys in total.

    Note that `nCm == nC(n-m)`, therefore the formula above is also equal to

        `num_buns` CHOOSE `num_buns - num_required + 1`
    
    This is related to the next variable, which will come in handy to simplify the code later

For the second variable, we follow the same logic:

    Since `num_required - 1` bunnies is missing 1 key, the rest of the bunnies
    must have that key. Therefore, there are:

        num_buns - (num_required - 1) = num_buns - num_required + 1

    copies of each distinct key.

With these variables, the remainder of our job is to distribute the (copies of the) keys 
to the bunnies in a lexicographically smallest order. Since we know each key must have k copies,
each key must be distributed to k bunnies. 

To meet the lexicographic requirement, conceptually we must give the smallest-indexed bunnies 
the smallest-indexed keys. That is, for example given 5 bunnies and 3 copies of each key:

    Key     Bunnies (3-Combinations)
     0      0, 1, 2
     1      0, 1, 3
     2      0, 1, 4
     3      0, 2, 3
     4      0, 2, 4
        ...

Luckily, the `itertools.combinations` function in Python already returns a sorted lexicographically
smallest list of k-combinations given a sorted input of keys. From here, we can simply assign
each key to the correct bunnies.



Source:
The majority of ideas are acquired from the following blogs and forum posts.
https://math.stackexchange.com/questions/4218959/is-there-a-way-of-constructing-a-set-of-sets-such-that-any-union-of-m-subsets
https://vitaminac.github.io/Google-Foobar-Free-the-Bunny-Prisoners/#Reference
'''

print(solution(2, 1))
print(solution(4, 4))
print(solution(5, 3))
