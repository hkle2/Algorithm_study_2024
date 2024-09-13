class Solution:
    def repeatedCharacter(self, s: str) -> str:
        answer = [s[0]]
        for i in range(1, len(s)):
            if s[i] in answer:
                return s[i]
            else:
                answer.append(s[i])