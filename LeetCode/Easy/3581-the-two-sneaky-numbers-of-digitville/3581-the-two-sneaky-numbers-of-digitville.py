class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer1 = []
        answer2 = []
        for i in range(len(nums)):
            if nums[i] not in answer1:
                answer1.append(nums[i])
            else:
                answer2.append(nums[i])
        return answer2
