class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for s in sentences:
            answer = max(answer, len(s.split(" ")))
        return answer

# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         answer = []
#         for s in sentences:
#             answer.append(len(s.split(" ")))
#         return max(answer)