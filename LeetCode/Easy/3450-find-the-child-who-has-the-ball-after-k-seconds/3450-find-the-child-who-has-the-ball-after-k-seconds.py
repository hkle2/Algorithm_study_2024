class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [x for x in range(n)]
        queue = children + children[1:-1][::-1]
        return queue[k % len(queue)]