class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        # s = set(nums)
        # print(len(s))
        n = len(nums)
        for i in range(n):
            for j in range(1, n):
                for k in range(2, n):
                    if i < j and j < k:
                        if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                            answer += 1

        return answer