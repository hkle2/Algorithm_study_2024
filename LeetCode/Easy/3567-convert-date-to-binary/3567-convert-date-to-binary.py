class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date_list = date.split("-")
        bin_date_list = []
        for num in date_list:
            bin_date_list.append(bin(int(num))[2:])
        return "-".join(bin_date_list)