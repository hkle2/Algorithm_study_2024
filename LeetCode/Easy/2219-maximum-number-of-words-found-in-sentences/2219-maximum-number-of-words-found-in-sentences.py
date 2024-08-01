# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         # 문자열 split, len, max
#         answer = 0
#         for sentence in sentences:
#             words = sentence.split(" ")
#             # words의 길이와 answer를 비교해서 더 큰 값을 answer로 지정
#             answer = max(len(words), answer)
#         return answer

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split(" ")) for sentence in sentences])

# class Solution:
#     def mostWordsFound(self, sentences: List[str]) -> int:
#         answer = []
#         for s in sentences:
#             answer.append(len(s.split(" ")))
#         return max(answer)