class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_nums = []
        for i in range(len(nums)):
            if i == 0:
                new_nums.append(nums[i])
            elif nums[i] != nums[i-1]:
                new_nums.append(nums[i])
        answer = 0
        for i in range(1, len(new_nums)-1):
            if new_nums[i-1] < new_nums[i] >new_nums[i+1]:
                answer += 1
            if new_nums[i-1] > new_nums[i] < new_nums[i+1]:
                answer += 1
        return answer

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                answer += 1
            if nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                answer += 1
        return answer