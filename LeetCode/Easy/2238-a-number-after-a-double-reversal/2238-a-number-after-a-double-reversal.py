# class Solution:
#     def isSameAfterReversals(self, num: int) -> bool:
#         reversed1 = int(str(num)[::-1])
#         # reversed_num을 다시 뒤집고 num과 비교해 보기
#         reversed2 = int(str(reversed1)[::-1])
#         if num == reversed2:
#             return True
#         return False

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = int("".join(reversed(str(num))))
        reversed2 = int("".join(reversed(str(reversed1))))
        if num == reversed2:
            return True
        return False