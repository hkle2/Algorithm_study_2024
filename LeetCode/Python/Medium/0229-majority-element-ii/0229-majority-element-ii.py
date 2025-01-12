from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []    
        n = len(nums)
        m = math.floor(n / 3)
        nums_counter = Counter(nums)
        for num, cnt in nums_counter.items():
            if cnt > m:
                answer.append(num)
        return answer

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            if nums.count(i) > len(nums) / 3:
                answer.append(i)
        answer = set(answer)
        return answer