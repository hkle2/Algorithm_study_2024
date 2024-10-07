class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d = {}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            d[divisor] = score
        max_score = max(d.values())
        candidates = []
        for divisor, score in d.items():
            if score == max_score:
                candidates.append(divisor)
        answer = sorted(candidates)[0]
        return answer

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d = {}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            d[divisor] = score
        answer = sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0]
        return answer

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        answer = 0
        d = {}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            d[divisor] = score
        answer = float("inf")
        for key, value in d.items():
            if value == max(d.values()):
                if key < answer:
                    answer = key
        return answer
        
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()
        answer = 0
        div = []
        for i in range(len(divisors)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    cnt += 1
            div.append(cnt)
        return divisors[div.index(max(div))]