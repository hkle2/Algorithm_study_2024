class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l_date = date.split("-")
        bin_date = []
        for num in l_date:
            bin_date.append(bin(int(num))[2:])
        return "-".join(bin_date)