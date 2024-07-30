class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # 각 divisor 별 divisibility score 저장
        d = {}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            d[divisor] = score
        max_score = max(d.values())
        answer = sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0]
        return answer

# class Solution:
#     def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
#         answer = 0
#         # 각 divisor 별 divisibility score 저장
#         d = {}
#         for divisor in divisors:
#             score = 0
#             for num in nums:
#                 # score 계산
#                 if num % divisor == 0:
#                     score += 1
#             d[divisor] = score
#         answer = float("inf")
#         for key, value in d.items():
#             if value == max(d.values()):
#                 if key < answer:
#                     answer = key
#         return answer

# class Solution:
#     def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
#         divisors.sort()
#         div = []
#         for d in range(len(divisors)):
#             cnt = 0
#             for j in range(len(nums)):
#                 if nums[j] % divisors[d] == 0:
#                     cnt += 1
#             div.append(cnt)
#         i = div.index(max(div))
#         return divisors[i]
