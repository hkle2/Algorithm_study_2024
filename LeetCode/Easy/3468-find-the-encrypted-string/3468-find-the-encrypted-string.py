class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        answer = ""
        for i in range(len(s)):
            n = (i + k) % len(s)
            answer += s[n]
        return answer
        