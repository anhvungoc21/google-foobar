import math


def letter_to_braille_components(letter):
    """
    Translates a letter to its corresponding Braille components:
    + Base (Possible values: 0-9, inclusive): Determines the top two rows
    + Increment (Possible values: 0-2, inclusive): Determines the bottom row
    
    The base is the column number in the `braille_layout` matrix
    The increment is the row number in the `braille_layout` matrix
    
    Args:
        `letter`: An English letter
    
    Returns: 
        A tuple containing the numeric values of the base and increment
    
    Throws:
        ValueError if input `letter` is not a lowercase English letter
    """
    
    # Braille has the same base pattern (First 2 rows) for
    # 10 consecutive letters (a-j, k-t) with an exception of 'w'
    BRAILLE_PATTERN_LENGTH = 10
    
    # A (10 x 3) matrix of letters arranged by their base pattern
    # Letters in the same column share the same base.
    braille_layout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                      'u', 'v', 'x', 'y', 'z', ' ', ' ', ' ', ' ', 'w']
    
    # Get the base and increment corresponding to letter
    index = braille_layout.index(letter)
    base = index % BRAILLE_PATTERN_LENGTH
    increment = math.floor(index / BRAILLE_PATTERN_LENGTH)
    return base, increment


def top_two_rows(base):
    """
    Translates the base number to a formattable Braille string. 
    This base string contains the top two rows of a Braille symbol, along
    with Python format brackets for conveniently inserting the bottom row later
    
    Args:
        `base`: A numeric value representing the base Braille
    
    Returns: 
        A formattable string that contains the top two rows in Braille
        and placeholders for the bottom row
    """
    
    base_to_braille_string = {
        0: "10{}00{}",
        1: "11{}00{}",
        2: "10{}10{}",
        3: "10{}11{}",
        4: "10{}01{}",
        5: "11{}10{}",
        6: "11{}11{}",
        7: "11{}01{}",
        8: "01{}10{}",
        9: "01{}11{}"
    }
    
    return base_to_braille_string[base]


def bottom_row(base, increment):
    """
    Translates the increment to the corresponding dots in 
    the bottom row of a Braille symbol. These dots can 
    be inserted into a base string to form the full symbol.
    
    Args:
        `base`: A numeric value representing the base in Braille
        `increment`: A numeric value representing the increment in Braille
    
    Returns: 
        A tuple containing the dots (1: bump, 0: flat)
        in the bottom row of a Braille symbol
    """
    
    # Handle "w" edge case separately
    if base == 9 and increment == 2: 
        return (0, 1)
        
    increment_to_encoding = {
        0: (0, 0),
        1: (1, 0),
        2: (1, 1)
    }
        
    return increment_to_encoding[increment]


def solution(s):
    """
    Translates a string `s` to its Braille representation
    
    Args:
        `s`: A string of English letters and spaces
    
    Returns: 
        A stringified Braille representation of string `s`
    """
    
    # Brailles for the space character 
    # and the signifier that precedes an  uppercase letter
    SPACE = "000000"
    UPPER_SIGNIFIER = "000001"
    
    # Encode each character in Braille
    result = []
    for char in s:
        # Handle space separately from letters
        if char == " ":
            result.append(SPACE)
            continue
        
        # Combine Braille components into full Braille encoding
        base, increment = letter_to_braille_components(char.lower())
        top_two_rows_str = top_two_rows(base)
        bottom_row_dots = bottom_row(base, increment)
        braille = top_two_rows_str.format(*bottom_row_dots)
        
        # Store result
        if char.isupper():
            result.append(UPPER_SIGNIFIER)
        result.append(braille)
    
    return "".join(result)