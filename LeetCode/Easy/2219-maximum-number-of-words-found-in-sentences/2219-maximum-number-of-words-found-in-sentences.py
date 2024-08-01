class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = []
        for s in sentences:
            answer.append(len(s.split(" ")))
        return max(answer)