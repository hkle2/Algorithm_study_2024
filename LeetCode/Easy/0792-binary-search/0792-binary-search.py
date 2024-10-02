class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1억 개의 숫자가 정렬된 nums
        # target: 1900
        # 알고리즘
        # 1. 중간에 위치한 숫자를 찾는다.
        # 2. target과 같다면 해당 위치가 정답
        # 3-1. 만약 target이 현재 위치의 숫자보다 크다면, 중간과 맨 끝 사이에 target이 존재할 것
        # 3-2. 만약 target이 현재 위치의 숫자보다 작다면, 처음과 중간 사이에 target이 존재할 것
        # 4. 후보군을 좁혀서 다시 1부터 시작
        l = 0
        r = len(nums) - 1
        answer = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] > target:
                # 현재 위치보다 왼쪽에 찾고자 하는 값이 있다.
                # 그러므로 r 값을 mid -1로 지정
                r = mid - 1
            else:
                # 현재 위치보다 오른쪽에 찾고자 하는 값이 있다.
                # 그러므로 l 값을 mid + 1로 지정
                l = mid + 1
        return answer

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums)-1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1