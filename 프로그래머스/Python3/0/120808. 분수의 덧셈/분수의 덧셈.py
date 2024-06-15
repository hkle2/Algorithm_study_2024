def solution(numer1, denom1, numer2, denom2):
    answer = []
    m = numer1 * denom2 + numer2 * denom1
    n = denom1 * denom2
    for i in range(m, 1, -1):
        if m % i == 0 and n % i == 0:
            m //= i
            n //= i
    answer.append(m)
    answer.append(n)
    return answer