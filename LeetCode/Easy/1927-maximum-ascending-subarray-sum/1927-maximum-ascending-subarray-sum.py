class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # 이전 수보다 증가하고 있는지를 체크
        # 계속 증가하고 있으면 현재의 누적합에 숫자 더해주기
        # 만약 감소한다면 현재의 누적합 초기화
        # answer와 현재 누적합 비교해서 더 큰 값을 answer로 지정
        prev = 0
        cur_sum = 0
        answer = 0
        for num in nums:
            if num > prev:
                # 현재 누적합에 숫자 더해줌
                # 누적합과 answer 비교, 더 큰 값을 지정
                cur_sum += num
            else:
                # cur_sum을 현재 숫자로 초기화
                cur_sum = num
            answer = max(answer, cur_sum)
            prev = num
        return answer

# class Solution:
#     def maxAscendingSum(self, nums: List[int]) -> int:
#         answer = nums[0]
#         sum_ = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i-1] < nums[i]:
#                 sum_ += nums[i]
#             else:
#                 sum_ = nums[i]
#             answer = max(answer, sum_)
#         return answer