def solution(l, t):
    # Obtain prefix sums
    for i in range(1, len(l)):
        l[i] += l[i - 1]

        # If sum is found, return because 0 is smallest start
        if l[i] == t:
            return [0, i]
    
    # Find smallest sublist that starts at other indicies
    left = right = 0
    while right < len(l):
        
        # Calculate sum of current window
        curSum = l[right] - l[left]
        
        # Return window indices if found sum
        if curSum == t:
            return [left + 1, right]
        
        # If sum exceeds target, reset and increment window
        if curSum > t:
            left += 1
            right = left + 1
        # Else, keep expanding window
        else:
            right += 1
    
    # Window has reached end of list. Shrink it incrementally
    right -= 1
    while left < len(l):
        
        # Return window indicies if found sum
        if l[right] - l[left] == t:
            return [left + 1, right]
        
        # Shrink window
        left += 1
    
    # Unable to find target
    return [-1, -1]


print(solution([1, 2, 3, 4], 15) == [-1, -1])

print(solution([4, 3, 10, 2, 8], 12) == [2, 3])
