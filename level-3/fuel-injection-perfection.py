def solution(n):
    n = int(n)

    ops = 0
    while n > 1:
        # Always divide when possible
        if n % 2 == 0:
            n //= 2
        # Number is "X01". See proof below.
        elif n == 3 or n % 4 == 1:
            n -= 1
        # Number is "X11". See proof below.
        else:
            n += 1
        
        ops += 1

    return ops

"""
========== Rationale ==========

This proof aims to demonstrate that for any input n, we can choose 
the optimal operation according to the following schema:

    1) If n is even, division is optimal.
    2) If n is odd,
        +) and the ending bits of n are "01", subtraction is optimal
        +) and the ending bits of n are "11", addition is optimal. Except when n = 3.

To achieve this, we first conceptualize the goal of our solution in terms of bits.
Since we want to arrive at 1 ("...01"), we can think of this process as iteratively
removing bits to the right of "...01" until we reach it. More importantly:

    +) Addition and subtraction do not change the number of bits
    +) Division reduces the number of bits by 1

Therefore, the process involves iteratively arriving at "desirable" numbers with one fewer bit.
Consider such an arbitrary iteration. Let "X" will be the binary representation of the so-called 
desirable number. We thus have two cases for the previous iteration:

    1) "X0" (an even number)
    2) "X1" (an odd number)

===== Case 1: "X0" =====
To arrive at "X", division is vacuously optimal because a division by 2 removes the least siginificant "0" bit.
Therefore, we always divide when the number is even.

===== Case 2: "X1" =====
Here, the available options are addition and subtraction, since division is prohibited for an odd number.
Consider two sub-cases:

    a) "X" is "Y0"      ==>      "X1" is "Y01"
    b) "X" is "Y1"      ==>      "X1" is "Y11"

=== Sub-case 2a: "Y01" ===
Unlike 2b, we are safe to consider only the last two bits because neither 
operations can affect other leftward bits, that is:

    - Addition:         "Y01" ---> "Y10"
    - Subtraction:      "Y01" ---> "Y00"

To arrive at "Y", the optimal paths are:

    - Addition first:       "Y01"  ---> "Y10" ---> "Y1" ---> "Y0" ---> "Y"
                                   (+)        (/)       (-)       (/)
    - Subtraction first:    "Y01"  ---> "Y00" ---> "Y0" ---> "Y"
                                   (-)        (/)       (/)

So, subtraction is never worse when the last two bits are "01".

=== Sub-case 2b: "Y11"
Here, while subtraction can only affect the last bit, addition might create a "ripple" effect
and mutate other leftward bits if they are consecutive "1"s. For example:

    "0111"  becomes "1000"

So, we need to consider a number with an arbitrary number of ending "1" bits to arrive at the correct
choice of operation. Instead of considering "Y11", we then consider the number "Z01...1", 
which has k ending bits set to "1". By its own definition, the (k + 1)th bit must be a "0".

If subtraction is used:
    
    "Z01...1"  ---> "Z01...0" ---> "Z01..." ---> ...
               (-)            (/)                (-) and (/)

To arrive at "Z0", we need to interleave k subtractions and k divisions.
The total number of operations is 2k.

If addition is used:

    "Z01...1"  ---> "Z10...0" ---> "Z10..." ---> ...
               (+)            (/)                (/) only

To arrive at "Z0", we only require one initial addition operation, which flips all
"1" bits to "0" bits. Then, we can repeatedly perform k division operations to arrive
at "Z1". Then, we subtract once more to "correct" the result into "Z0". The total number
of operations is:

    1 + k + 1 = k + 2

For any k > 1, using addition is optimal because k + 2 < 2k. 

When k = 1, 1 + 2 > 2. Therefore, using subtraction is optimal in this singular case.
While this may appear contradictory (we are considering "Z01...1", yet there must only be
one "1" bit), this special case directly corresponds to "011" (natural: 3). To verify this:

    - Subtraction:      "011" ---> "010" ---> "01" = 1
                              (-)        (/)
    - Addition:         "011" ---> "100" ---> "10" ---> "1" = 1
                              (+)        (/)       (/)

Subtraction indeed is optimal when the input is 3.

We have therefore shown the optimal choice of operation for all possible input n.


Reference:
- Inspiration to consider the last bits from StackOverflow thread: 
https://stackoverflow.com/questions/39588554/minimum-number-of-steps-to-reduce-number-to-1/57386889#57386889

- Improvement: This proof that I wrote (hopefully) introduces a more intuitive and structured
way of approaching this problem. Instead of looking at the last 3 bits and deriving the specific
number of operations, we only look at 2 bits and consider the special "ripple" effect.
"""


print(solution("15"))
print(solution("4"))




# DP
# from collections import deque

# def solution(n):
#     n = int(n)

#     # DP Table
#     table = [float("inf") for _ in range(n + 2)]

#     # DP
#     to_visit = deque([(n, 0)])
#     while to_visit:
#         num, depth = to_visit.popleft()

#         # Greedily divide if possible
#         while num % 2 == 0:
#             num = num // 2
#             depth += 1
#         table[num] = min(table[num], depth)

#         # Search options
#         options = [num + 1, num - 1]
#         new_depth = depth + 1

#         # Explore option
#         for opt in options:
#             if opt > 0 and new_depth < table[opt]:
#                 table[opt] = new_depth
#                 to_visit.append((opt, new_depth))

#     return table[1]



