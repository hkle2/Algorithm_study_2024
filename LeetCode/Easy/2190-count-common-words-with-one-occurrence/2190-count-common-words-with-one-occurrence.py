from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        for w, i in Counter(words1).items():
            if i == 1:
                if Counter(words2).get(w, 0) == 1:
                    answer += 1
        return answer