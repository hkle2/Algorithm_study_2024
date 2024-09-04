class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        # 반복하면서 양수하나, 음수 하나 넣어주면 됨
        # 1, -1, 2, -2
        # 만약에 n이 홀수라면 0을 하나 넣어주면 됨
        if n % 2 == 1:
            answer.append(0)
        for i in range(n//2):
            answer.append(i+1)
            answer.append(-(i+1))
        return answer

# class Solution:
#     def sumZero(self, n: int) -> List[int]:
#         return [i for i in range(-n+1, n, 2)]

# class Solution:
#     def sumZero(self, n: int) -> List[int]:
#         answer = []
#         for i in range(1, n//2+1):
#             answer.append(i)
#             answer.append(-i)
#         if n % 2 != 0:
#             answer.append(0)
#         return answer