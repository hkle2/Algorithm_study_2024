# class Solution:
#     def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         # set, dict
#         rank_dict = {x: (i + 1) for i, x in enumerate(sorted(set(arr)))}
#         print(rank_dict)
#         return []

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = []
        sorted_arr = sorted(set(arr))
        rank = {}
        for i, n in enumerate(sorted_arr):
            rank[n] = i+1
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