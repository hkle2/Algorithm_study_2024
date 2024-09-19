class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        ball_loc = 0
        received = [0]
        i = 1
        while True:
            ball_loc = (ball_loc + i * k) % n
            if ball_loc not in received:
                received.append(ball_loc)
                i += 1
            else:
                break
        return [i+1 for i in range(n) if i not in received]