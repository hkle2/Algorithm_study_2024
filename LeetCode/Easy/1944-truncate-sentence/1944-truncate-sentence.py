class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split()
        l = l[:k]
        answer = ' '.join(l)
        return answer