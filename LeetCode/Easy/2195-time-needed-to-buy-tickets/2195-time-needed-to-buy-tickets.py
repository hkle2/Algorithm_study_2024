class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] < tickets[k]:
                    answer += tickets[i]
                else:
                    answer += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    answer += tickets[i]
                else:
                    answer += (tickets[k] - 1)
        return answer

# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         time = 0
#         for i in range(len(tickets)):
#             if tickets[i] >= tickets[k]:
#                 if i <= k:
#                     time += tickets[k]
#                 else:
#                     time += tickets[k] - 1
#             else:
#                 time += tickets[i]
#         return time

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