class Solution:
    def minimumMoves(self, s: str) -> int:
        s = list(s)
        n = len(s)
        answer = 0
        for i in range(n-2):
            if s[i] == "O" and (i+2 <= n-2):
                continue
            cnt = 0
            for j in range(3):
                if s[i+j] == "X":
                    s[i+j] = "O"
                    cnt += 1
            if cnt != 0:
                answer += 1
            if "X" not in s:
                return answer
        return answer
        