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

import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    m = numer1 * denom2 + numer2 * denom1
    n = denom1 * denom2
    gcd = math.gcd(m, n)
    m //= gcd
    n //= gcd
    answer.append(m)
    answer.append(n)
    return answer

from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = []
    f = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer.append(f.numerator)
    answer.append(f.denominator)
    return answer