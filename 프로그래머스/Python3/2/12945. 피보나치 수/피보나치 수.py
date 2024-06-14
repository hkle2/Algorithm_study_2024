def solution(n):
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a + b
    answer = a % 1234567
    return answer

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i - 2] + dp[i - 1]
    answer = dp[n] % 1234567
    return answer