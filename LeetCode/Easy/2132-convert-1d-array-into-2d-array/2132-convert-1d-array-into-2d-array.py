class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        answer = []
        cnt = len(original)
        if cnt != m * n:
            return answer
        for i in range(0, len(original), n):
            answer.append(original[i:i+n])
        return answer

# class Solution:
#     def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
#         answer = []
#         if len(original) == m * n:
#             for i in range(0, len(original), n):
#                 answer.append(original[i:i+n])
#         else:
#             return []
#         return answer