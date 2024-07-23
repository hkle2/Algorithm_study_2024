class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        i = 1
        while x > 0 and y > 0:
            x -= 1
            y -= 4
            if x >= 0 and y >= 0:
                i += 1
        if i % 2 == 0:
            return "Alice"
        return "Bob"