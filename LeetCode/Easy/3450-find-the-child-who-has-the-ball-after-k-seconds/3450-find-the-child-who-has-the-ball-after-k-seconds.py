class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        div, mod = divmod(k, n-1)
        if div % 2 == 0:
            return mod
        return n - 1 - mod

# class Solution:
#     def numberOfChild(self, n: int, k: int) -> int:
#         children = [x for x in range(n)]
#         line = children + children[1:-1][::-1]
#         return line[k % len(line)]