class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = ""
        prev = ""
        cnt = 0
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                answer += c
            prev = c
        return answer

class Solution:
    def makeFancyString(self, s: str) -> str:
        seen = []
        for i in range(len(s)):
            if (len(seen) >= 2) and (s[i] == seen[-1]) and (s[i] == seen[-2]):
                continue
            else:
                seen.append(s[i])
        return "".join(seen)