class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = 0
        cur = 0
        for i in word:
            if abs(cur - (ord(i) - ord("a"))) <= 13:
                answer += abs(cur - (ord(i) - ord("a"))) + 1
            else:
                answer += 26 - abs(cur - (ord(i) - ord("a"))) + 1
            cur = ord(i) - ord("a")
        return answer