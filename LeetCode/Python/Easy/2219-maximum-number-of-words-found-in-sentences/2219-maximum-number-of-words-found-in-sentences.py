class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            words = sentence.split(" ")
            answer = max(len(words), answer)
        return answer

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split(" ")) for sentence in sentences])

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = []
        for s in sentences:
            answer.append(len(s.split(" ")))
        return max(answer)