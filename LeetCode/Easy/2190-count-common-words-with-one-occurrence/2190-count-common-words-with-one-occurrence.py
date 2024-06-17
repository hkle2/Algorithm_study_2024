from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        for w1, i in cnt1.items():
            if i == 1:
                if cnt2.get(w1, 0) == 1:
                    answer += 1
        return answer