def solution(pegs):
    total = 0
    sign = 1

    # Arrive at `total = r0 +/- rn`
    # by eliminating intermediary pegs
    for i in range(1, len(pegs)):
        distance = pegs[i] - pegs[i-1]
        total += sign * distance
        sign *= -1

    # Radius must be a positive number, and so is total
    if total <= 0:
        return [-1, -1]
    
    # Refer to explanation below for the derivation of these formulas
    # + No. pegs odd: r0 = 2total
    # + No. pegs even: r0 = 2total/3
    a = 2 * total
    b = 3 if (len(pegs) % 2 == 0) else 1

    # Simplify fraction if necessary
    if (a % 3 == 0) and (b % 3 == 0):
        a /= 3
        b /= 3
    
    # Verify that no gears have non-positive radius
    radius = a/b
    for i in range(1, len(pegs)):
        distance = pegs[i] - pegs[i - 1]

        # Gear extends from this peg to next peg
        # The next peg therefore has no room for a gear. Invalid!
        if radius >= distance:
            return [-1, -1]
        
        # The previous radius determines the next
        radius = distance - radius

    # Verify that a >= b
    return [a, b] if a >= b else [-1, -1]


"""
===== Mathematical Rationale =====

To solve for the first radius (r0) and last radius (rn),
we need to find two 2-variable equations. We already have the first: 
    r0 = 2 * rn

We derive the second equation by combining the (n - 1) equations
relating to the distances in between pegs. Notice that:
    r0 + r1 = C1
    r1 + r2 = C2
    r2 + r3 = C3
    ...
    rn-1 + rn = Cn
where Cs are known constant distances between any two adjacent pegs.
We can eliminate the intermediary terms by interleaving additions 
and subtractions of these equations:
    (r0 + r1) - (r1 + r2) + (r2 + r3) - ... +/- (rn-1 + rn) = C1 - C2 + C3 - ... +/- Cn
<=> r0 +/- rn = some constant C
We thus have our second equation! 

Whether a plus or minus sign precedes the rn term is directly answered 
by whether the number of pegs are odd (-) or even (+).

With the two equations acquired, we trivially solve for r0 in each case:
    Odd:
        r0 - rn = C
        r0 = 2rn
    =>  rn = C, r0 = 2C

    Even:
        r0 + rn = C
        r0 = 2rn
    => rn = C/3, r0 = 2C/3
"""
