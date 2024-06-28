class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split()[:k]
        return " ".join(l)