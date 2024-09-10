class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [x for x in range(n)]
        line = children + children[1:-1][::-1]
        return line[k % len(line)]