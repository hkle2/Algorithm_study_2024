class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # k번째 사람이 사고 싶어 하는 티켓 수와 
        # 특정 위치의 사람이 티켓 사고 싶어 하는 수 비교
        # 해당 위치가 k보다 앞인지 뒤인지
        # 앞에 있는데 사고 싶은 티켓 수가 작은 경우
        # 앞에 있는데 사고 싶은 티켓이 많은 경우
        # 뒤에 있는데 사고 싶은 티켓이 많은 경우
        # 뒤에 있는데 사고 싶은 티켓이 작은 경우
        answer = 0
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] < tickets[k]:
                    answer += tickets[i]
                else:
                    # 내가 사고 싶은 양을 살 때까지 내 앞에 있음
                    answer += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    # 자기 사고 싶은 만큼만 사고 떠남
                    answer += tickets[i]
                else:
                    # 내가 사고 싶은 양 살 때까지 줄에 머무는데, 나보다 뒤에 있어서
                    # 내가 다 사게 되는 시점에는 이 사람을 안 기다려도 됨
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