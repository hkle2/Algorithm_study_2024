class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        answer = 0
        d = defaultdict(Counter)
        for p, c in pick:
            d[p][c] += 1
        print(d)
        for key, value in d.items():
            for i in value:
                if value[i] >= key + 1:
                    answer += 1
                    break
        return answer

# class Solution:
#     def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
#         answer = 0
#         d = defaultdict(Counter)
#         for p, c in pick:
#             d[p] += Counter(str(c))
#         print(d)
#         for key, value in d.items():
#             for i in value:
#                 if value[i] >= key + 1:
#                     answer += 1
#                     break
#         return answer