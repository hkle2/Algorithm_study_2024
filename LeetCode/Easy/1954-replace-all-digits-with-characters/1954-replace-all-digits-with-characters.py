class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        if len(s) % 2 == 0:
            for i in range(0, len(s), 2):
                answer += s[i] + chr(ord(s[i]) + int(s[i+1]))
        else:
            for i in range(0, len(s)-1, 2):
                answer += s[i] + chr(ord(s[i]) + int(s[i+1]))
            answer += s[-1]
        return answer