class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        s, e = nums.index(1), nums.index(n)
        if s < e:
            return s + (n - 1) - e
        else:
            return s + (n - 2) - e