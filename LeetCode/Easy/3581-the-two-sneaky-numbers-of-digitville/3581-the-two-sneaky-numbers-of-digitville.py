from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [key for key, value in Counter(nums).items() if value == 2]

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        c = Counter(nums)
        for key, value in c.items():
            if value == 2:
                answer.append(key)
        return answer

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = []
        answer = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                answer.append(nums[i])
        return answer