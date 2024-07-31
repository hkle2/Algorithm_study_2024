class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # for문, sorted, pop
        for i in range(k):
            gifts = sorted(gifts)
            max_gifts = gifts.pop()
            # 가져온 가장 큰 값에 제곱근을 취해서 다시 gifts에 append
            gifts.append(int(math.sqrt(max_gifts)))
        return sum(gifts)

# class Solution:
#     def pickGifts(self, gifts: List[int], k: int) -> int:
#         answer = 0
#         for i in range(k):
#             gifts.sort(reverse=True)
#             gifts[0] = int(gifts[0]**0.5)
#         answer = sum(gifts)
#         return answer