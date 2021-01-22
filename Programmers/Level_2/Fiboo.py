# Iterative Top-down으로 풀면 stack overflow를 방지할 수 있다.

def solution(n):
    def fib(N):
        if N <= 1:
            return N
        if N == 2:
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        for i in range(3, N + 1):
            current = (prev1 + prev2)%1234567
            prev2 = prev1
            prev1 = current
        return current

    return fib(n)

print(solution(100000))