class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1, n+1):
            cnt = 0
            for j in nums:
                if j >= i:
                    cnt += 1
            if cnt == i:
                return cnt
        return -1