class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [x for x in range(n)]
        queue = children + children[1:-1][::-1]
        return queue[k % len(queue)]

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        div, mod = divmod(k, n-1)
        if div % 2 == 0:
            return mod
        else:
            return n - 1 - mod