class Solution:
    def clearDigits(self, s: str) -> str:
        while s:
            flag = False
            for i, c in enumerate(s):
                if c.isnumeric():
                    flag = True
                    if i == 0:
                        s = s[i+1:]
                    else:
                        s = s[:i-1] + s[i+1:]
                    break
            if not flag:
                break
        return s

class Solution:
    def clearDigits(self, s: str) -> str:
        answer = []
        for i in s:
            if i.isdigit():
                answer.pop()
            else:
                answer.append(i)
        return "".join(answer)
