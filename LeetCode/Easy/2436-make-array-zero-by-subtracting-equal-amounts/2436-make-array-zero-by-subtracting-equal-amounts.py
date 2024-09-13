class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num})

# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         return len(set(filter(lambda x: x > 0, nums)))