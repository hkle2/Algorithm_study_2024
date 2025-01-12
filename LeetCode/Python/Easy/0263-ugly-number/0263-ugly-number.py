class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [2, 3, 5]
        while True:
            if n == 1:
                break
            flag = False
            for factor in factors:
                if n % factor == 0:
                    flag = True
                    n /= factor
                    break
            return flag
        return True

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n /= i
            if n == 1:
                return True

class Solution:
    def isUgly(self, n: int) -> bool:
        while True:
            if n == 0:
                return False
            if n == 1:
                return True
            elif n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False