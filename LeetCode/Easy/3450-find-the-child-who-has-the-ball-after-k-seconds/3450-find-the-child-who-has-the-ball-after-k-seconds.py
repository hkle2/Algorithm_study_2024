class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [i for i in range(n)]
        queue = children + children[1:-1][::-1]
        return queue[k % len(queue)]

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        return ([i for i in range(n)] + [i for i in range(n)][1:-1][::-1])[k % (2 * n - 2)]

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        div, mod = divmod(k, n-1)
        if div % 2 == 0:
            return mod
        else:
            return n - 1 - mod