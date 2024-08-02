class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num == target:
                answer.append(i)
        return answer

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [i for i, x in enumerate(sorted(nums)) if x == target]

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                answer.append(i)
        return answer