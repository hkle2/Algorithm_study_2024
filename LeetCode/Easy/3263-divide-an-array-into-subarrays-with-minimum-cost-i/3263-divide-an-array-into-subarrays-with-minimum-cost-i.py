class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = float("inf")
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                part_one = nums[:i]
                part_two = nums[i:j]
                part_three = nums[j:]
                current_cost = part_one[0] + part_two[0] + part_three[0]
                answer = min(answer, current_cost)
        return answer

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = []
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                answer.append(nums[0] + nums[i] + nums[j])
        return min(answer)