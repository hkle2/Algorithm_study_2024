class Solution:
    def clearDigits(self, s: str) -> str:
        answer = []
        for i in s:
            if i.isdigit():
                answer.pop()
            else:
                answer.append(i)
        return "".join(answer)
