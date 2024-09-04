class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        str_1 = s1[2] + s1[1] + s1[0] + s1[3]
        str_2 = s1[0] + s1[3] + s1[2] + s1[1]
        str_3 = s1[2] + s1[3] + s1[0] + s1[1]
        # s2와 일치하는 게 하나라도 있으면 True, 없으면 False
        if s2 == s1 or s2 == str_1 or s2 == str_2 or s2 == str_3:
            return True
        return False

# class Solution:
#     def canBeEqual(self, s1: str, s2: str) -> bool:
#         return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])

# class Solution:
#     def canBeEqual(self, s1: str, s2: str) -> bool:
#         l_s1 = list(s1)
#         l_s2 = list(s2)
#         if l_s1 == l_s2:
#             return True
#         l_s1[0], l_s1[2] = l_s1[2], l_s1[0]
#         if l_s1 == l_s2:
#             return True
#         l_s1[1], l_s1[3] = l_s1[3], l_s1[1]
#         if l_s1 == l_s2:
#             return True
#         l_s1[0], l_s1[2] = l_s1[2], l_s1[0]
#         if l_s1 == l_s2:
#             return True
#         return False