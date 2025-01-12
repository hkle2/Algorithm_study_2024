class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0
        for upper, percent in brackets:
            if upper <= income:
                amount = upper - prev
                answer += (amount * (percent / 100))
                prev = upper
            else:
                amount = income - prev
                answer += (amount * (percent / 100))
                break
        return answer

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