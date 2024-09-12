class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = []
        rank_dict = {x: (i + 1) for i, x in enumerate(sorted(set(arr)))}
        return [rank_dict[num] for num in arr]

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