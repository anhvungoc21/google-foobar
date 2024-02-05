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

print(solution("4", "7"))  # 4

print(solution("2", "1"))  # 1

print(solution("2", "4"))  # impossible

print(solution("1", "1"))  # 0
