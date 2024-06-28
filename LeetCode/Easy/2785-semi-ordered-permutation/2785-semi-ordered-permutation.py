class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        s, e = nums.index(1), nums.index(n)
        if s < e:
            answer = s + (n - 1) - e
        else:
            answer = s + (n - 2) - e
        return answer