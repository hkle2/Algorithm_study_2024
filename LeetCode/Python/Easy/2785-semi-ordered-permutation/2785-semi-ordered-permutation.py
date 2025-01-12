class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        first_index = nums.index(1)
        last_index = nums.index(len(nums))
        if first_index < last_index:
            answer = first_index + (len(nums) - 1 - last_index)
        else:
            answer = first_index + (len(nums) - 1 - last_index) - 1
        return answer

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        s, e = nums.index(1), nums.index(n)
        if s < e:
            return s + (n - 1) - e
        else:
            return s + (n - 2) - e