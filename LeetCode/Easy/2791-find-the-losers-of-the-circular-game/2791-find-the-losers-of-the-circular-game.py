# class Solution:
#     def circularGameLosers(self, n: int, k: int) -> List[int]:
#         # while, set
#         cur_loc = 0
#         visited = set([cur_loc])
#         while True:
#             # 한 번이라도 공을 잡았던 친구가
#             # 다시 공을 잡으면 break
#             pass
#         # 공을 한 번도 못 잡은 친구들을 answer에 담아서 리턴!
#         answer = []
#         return answer

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        friends = [False for _ in range(n)]
        ball_loc = 0
        i = 1
        while not friends[ball_loc]:
            friends[ball_loc] = True
            ball_loc = (ball_loc + i * k) % n
            i += 1
        return [i + 1 for i in range(n) if not friends[i]]

# class Solution:
#     def circularGameLosers(self, n: int, k: int) -> List[int]:
#         ball_loc = 0
#         received = [0]
#         i = 1
#         while True:
#             ball_loc = (ball_loc + i * k) % n
#             if ball_loc not in received:
#                 received.append(ball_loc)
#                 i += 1
#             else:
#                 break
#         return [i + 1 for i in range(n) if i not in received]