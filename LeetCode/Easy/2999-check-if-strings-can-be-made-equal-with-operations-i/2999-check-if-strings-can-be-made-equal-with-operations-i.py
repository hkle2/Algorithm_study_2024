class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])

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

# class Solution:
#     def canBeEqual(self, s1: str, s2: str) -> bool:
#         flag = True
#         odd = []
#         even = []
#         odd.append(s1[0])
#         odd.append(s1[2])
#         even.append(s1[1])
#         even.append(s1[3])
#         for i in range(len(s2)):
#             if i % 2 == 0:
#                 if s2[i] not in odd:
#                     flag = False
#             else:
#                 if s2[i] not in even:
#                     flag = False
#         return flag