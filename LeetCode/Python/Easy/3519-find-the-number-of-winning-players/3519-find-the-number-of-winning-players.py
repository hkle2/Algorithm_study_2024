class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        answer = 0
        d = defaultdict(Counter)
        for player, ball_color in pick:
            d[player][ball_color] += 1
        for player, ball_counter in d.items():
            if player + 1 <= max(ball_counter.values()):
                answer += 1
        return answer

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        answer = 0
        d = defaultdict(Counter)
        for p, c in pick:
            d[p][c] += 1
        for key, value in d.items():
            for i in value:
                if value[i] >= key + 1:
                    answer += 1
                    break
        return answer