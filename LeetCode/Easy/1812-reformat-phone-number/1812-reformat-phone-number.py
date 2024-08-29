class Solution:
    def reformatNumber(self, number: str) -> str:
        # replace, slice
        answer = []
        number = number.replace(" ", "")
        number = number.replace("-", "")
        while len(number) > 4:
            answer.append(number[:3])
            number = number[3:]
        # 2 digits: A single block of length 2.
        # 3 digits: A single block of length 3.
        # 4 digits: Two blocks of length 2 each.
        if len(number) == 4:
            answer.append(number[:2])
            answer.append(number[2:])
        else:
            answer.append(number)
        return "-".join(answer)

# class Solution:
#     def reformatNumber(self, number: str) -> str:
#         l = []
#         for num in number:
#             if num.isdigit():
#                 l.append(num)
#         print(l)
#         for i in range(0, len(l), 3):
#             num[i:i+3]
#         return ""

# class Solution:
#     def reformatNumber(self, number: str) -> str:
#         answer = []
#         number = number.replace(" ", "")
#         number = number.replace("-", "")
#         if len(number) % 3 == 0:
#             for i in range(0, len(number), 3):
#                 answer.append(number[i:i+3])
#         elif len(number) % 3 == 1:
#             for i in range(0, len(number)-4, 3):
#                 answer.append(number[i:i+3])
#             answer.append(number[-4:-2])
#             answer.append(number[-2:])
#         else:
#             for i in range(0, len(number)-2, 3):
#                 answer.append(number[i:i+3])
#             answer.append(number[-2:])
#         return "-".join(answer)