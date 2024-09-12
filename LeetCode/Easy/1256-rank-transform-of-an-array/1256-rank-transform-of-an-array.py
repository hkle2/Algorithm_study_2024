class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = []
        l_s = sorted(list(set(arr)))
        rank = {}
        for i, s in enumerate(l_s):
            rank[s] = i+1
        for num in arr:
            answer.append(rank[num])
        return answer

# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         answer = []
#         s = sorted(list(set(arr)))
#         for num in arr:
#             answer.append(s.index(num)+1)
#         return answer