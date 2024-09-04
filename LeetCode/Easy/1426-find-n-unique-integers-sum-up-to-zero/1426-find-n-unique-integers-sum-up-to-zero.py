class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        if n % 2 == 1:
            answer.append(0)
        for i in range(n//2):
            answer.append(i+1)
            answer.append(-(i+1))
        return answer

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(-n+1, n, 2)]

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for i in range(1, n//2+1):
            answer.append(i)
            answer.append(-i)
        if n % 2 != 0:
            answer.append(0)
        return answer