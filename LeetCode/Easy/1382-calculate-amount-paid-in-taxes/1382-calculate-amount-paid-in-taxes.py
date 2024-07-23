class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0
        for u, p in brackets:
            if u <= income:
                answer += (u - prev) * p / 100
                prev += (u - prev)
            else:
                answer += (income - prev) * p / 100
                break
        return answer