class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        tmp = ""
        for c in word:
            if c.isnumeric():
                tmp += c
            elif tmp:
                nums.add(int(tmp))
                tmp = ""
        if tmp:
            nums.add(int(tmp))
        return len(nums)

# class Solution:
#     def numDifferentIntegers(self, word: str) -> int:
#         answer = []
#         tmp = ""
#         for w in word:
#             if w.isnumeric():
#                 tmp += w
#             elif tmp:
#                 answer.append(tmp)
#                 tmp = ""
#         if tmp:
#             answer.append(tmp)
#         for i in range(len(answer)):
#             answer[i] = int(answer[i])
#         return len(set(answer))

# class Solution:
#     def numDifferentIntegers(self, word: str) -> int:
#         tmp = ""
#         for w in word:
#             if not w.isnumeric():
#                 word = word.replace(w, " ")
#         l = word.split()
#         for i in range(len(l)):
#             l[i] = int(l[i])
#         return len(set(l))