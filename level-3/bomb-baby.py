def solution(x, y):
    x = int(x)
    y = int(y)

    big, small = max(x, y), min(x, y)

    steps = 0
    while big >= 1 and small >= 1:
        quotient, remainder = divmod(big, small)
        big, small = small, remainder
        steps += quotient

    return str(steps - 1) if (big == 1 and small == 0) else "impossible"


# def solution(x, y):
#     x, y = int(x), int(y)

#     # Base case
#     if x == 1 and y == 1: return "0"

#     # Matrix y rows, x columns
#     seen = [[0 for _ in range(x + 1)] for _ in range(y + 1)]

#     # Start
#     to_visit = [(1, 1, 0)]

#     # DP
#     while to_visit:
#         row, col, depth = to_visit.pop()

#         # Invalid index. Skip!
#         if row > y or col > x: continue

#         # Seen. Maybe found a shorter path!
#         if seen[row][col] != 0:
#             seen[row][col] = min(seen[row][col], depth)
#             continue

#         # Mark current position as visited
#         seen[row][col] = depth

#         # Search both paths
#         to_visit.append((row + col, col, depth + 1))
#         to_visit.append((row, row + col, depth + 1))

#     result = seen[y][x]
#     return str(result) if (result > 0) else "impossible"

print(solution("4", "7"))  # 4

print(solution("2", "1"))  # 1

print(solution("2", "4"))  # impossible

print(solution("1", "1"))  # 0
