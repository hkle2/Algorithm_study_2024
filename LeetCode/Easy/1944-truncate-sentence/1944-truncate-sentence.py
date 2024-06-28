class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        word_list = s.split(" ")
        return " ".join(word_list[:k])

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split()[:k]
        return " ".join(l)