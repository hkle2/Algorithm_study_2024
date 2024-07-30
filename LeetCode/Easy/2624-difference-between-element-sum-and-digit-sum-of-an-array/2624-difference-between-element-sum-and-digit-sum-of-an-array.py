class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # for문으로 반복
        # num을 문자열로 만들고, 다시 for문을 돌면 각 자릿수를 가져올 수 있음
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for c in str(num):
                digit_sum += int(c)
        # 둘의 차이의 절대값을 리턴
        return abs(element_sum - digit_sum)

# class Solution:
#     def differenceOfSum(self, nums: List[int]) -> int:
#         x = sum(nums)
#         y = 0
#         for num in nums:
#             for n in str(num):
#                 y += int(n)
#         return abs(x - y)
        