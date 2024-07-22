class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        for i in range(0, len(s)-1, 2):
            answer += s[i] + chr(ord(s[i]) + int(s[i+1]))
        if len(s) % 2 != 0:
            answer += s[-1]
        return answer