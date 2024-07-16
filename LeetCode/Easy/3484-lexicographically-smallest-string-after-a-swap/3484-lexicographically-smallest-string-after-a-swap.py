class Solution:
    def getSmallestString(self, s: str) -> str:
        answer = [s]
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                swaped = s[:i] + s[i+1] + s[i] + s[i+2:]
                answer.append(swaped)
        return sorted(answer)[0]

class Solution:
    def getSmallestString(self, s: str) -> str:
        answer = [s]
        for i in range(len(s)-1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                answer.append(s[:i] + s[i+1] + s[i] + s[i+2:])
        answer.sort()
        return answer[0]