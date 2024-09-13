class Solution:
    def repeatedCharacter(self, s: str) -> str:
        answer = []
        for i in range(len(s)):
            if s[i] in answer:
                return s[i]
            else:
                answer.append(s[i])