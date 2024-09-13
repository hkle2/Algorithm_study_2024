class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 규칙 찾기
        # 0이 아닌 유니크한 숫자 개수
        element = set()
        for num in nums:
            if num > 0:
                element.add(num)
        return len(element)
        
# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         return len({num for num in nums if num})

# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         return len(set(filter(lambda x: x > 0, nums)))