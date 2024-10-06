class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         for i, num1 in enumerate(nums):
#             for j in range(i+1, length):
#                 if num1 + nums[j] == target:
#                     return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         for i, num1 in enumerate(nums):
#             for j in range(i+1, length):
#                 if num1 + nums[j] == target:
#                     return [i, j]
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # 1. 2중 for문을 사용하는 방식
#         # 2. 1중 for문 만으로 해결하는 방식
#         # for i in range(len(nums)):
#         #     for j in range(i+1, len(nums)):
#         #         if nums[i] + nums[j] == target:
#         #             return [i, j]
#         d = defaultdict(list)
#         for i, num in enumerate(nums):
#             d[num].append(i)
#         print(d)

#         for i, num in enumerate(nums):
#             # 1. 현재 숫자와 더해서 target이 되는 숫자 구하기
#             # 2. 그 숫자가 dictionary 안에 들어있는지 체크하기
#             # 3. 들어있고, 현재 숫자와 target에서 빼준 숫자가 동일한지 체크, 예외처리
#         return []