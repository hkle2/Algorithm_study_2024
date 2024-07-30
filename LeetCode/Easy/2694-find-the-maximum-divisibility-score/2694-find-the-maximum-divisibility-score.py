class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()
        div = []
        for i in range(len(divisors)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    cnt += 1
            div.append(cnt)
        return divisors[div.index(max(div))]
