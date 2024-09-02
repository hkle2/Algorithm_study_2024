class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        if (ord(x1) + int(y1)) % 2 == (ord(x2) + int(y2)) % 2:
            return True
        return False

# class Solution:
#     def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
#         col1 = "aceg"
#         col2 = "bdfh"
#         if int(coordinate1[1]) % 2 == int(coordinate2[1]) % 2:
#             if (coordinate1[0] in col1 and coordinate2[0] in col1) or (coordinate1[0] in col2 and coordinate2[0] in col2):
#                 return True
#         else:
#             if (coordinate1[0] in col1 and coordinate2[0] in col2) or (coordinate1[0] in col2 and coordinate2[0] in col1):
#                 return True
#         return False