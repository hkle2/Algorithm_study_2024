class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # k번째 사람이 사고 싶어 하는 티켓 수와 
        # 특정 위치의 사람이 티켓 사고 싶어 하는 수 비교
        # 해당 위치가 k보다 앞인지 뒤인지
        time = 0
        for i in range(len(tickets)):
            if tickets[i] >= tickets[k]:
                if i <= k:
                    time += tickets[k]
                else:
                    time += tickets[k] - 1
            else:
                time += tickets[i]
        return time



# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         n = len(tickets)
#         i = 0
#         time = 0
#         while tickets[k] != 0:
#             i %= n
#             if tickets[i] != 0:
#                 tickets[i] -= 1
#                 time += 1
#             i += 1
#         return time