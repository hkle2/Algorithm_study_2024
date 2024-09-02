class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col1 = "aceg"
        col2 = "bdfh"
        if (int(coordinate1[1]) % 2 == 0) == (int(coordinate2[1]) % 2 == 0):
            if (coordinate1[0] in col1 and coordinate2[0] in col1) or (coordinate1[0] in col2 and coordinate2[0] in col2):
                return True
        else:
            if (coordinate1[0] in col1 and coordinate2[0] in col2) or (coordinate1[0] in col2 and coordinate2[0] in col1):
                return True
        return False