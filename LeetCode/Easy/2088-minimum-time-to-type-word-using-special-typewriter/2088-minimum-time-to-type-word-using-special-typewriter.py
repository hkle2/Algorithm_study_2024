class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = 0
        loc = 0
        for c in word:
            target_loc = ord(c) - 97
            move = abs(target_loc - loc)
            move_reverse = 26 - abs(target_loc - loc)
            answer += min(move, move_reverse) + 1
            loc = target_loc
        return answer

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