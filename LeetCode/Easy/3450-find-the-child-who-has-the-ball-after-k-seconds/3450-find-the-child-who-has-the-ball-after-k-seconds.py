class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # modulo, children list를 만든 다음, 뒤집어서 한번 붙이기
        children = [x for x in range(n)]
        queue = children + children[1:-1][::-1]
        # k가 queue 길이보다 작을 때는 그냥 k번째 element 리턴
        # k가 queue 길이보다 클 때는 모듈로 적용
        return queue[k % len(queue)]

# class Solution:
#     def numberOfChild(self, n: int, k: int) -> int:
#         children = [x for x in range(n)]
#         line = children + children[1:-1][::-1]
#         return line[k % len(line)]

# class Solution:
#     def numberOfChild(self, n: int, k: int) -> int:
#         div, mod = divmod(k, n-1)
#         if div % 2 == 0:
#             return mod
#         else:
#             return n - 1 - mod