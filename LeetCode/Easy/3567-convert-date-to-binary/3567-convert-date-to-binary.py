class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split("-")
        year_bin = bin(int(year))[2:]
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]
        return f"{year_bin}-{month_bin}-{day_bin}"

# class Solution:
#     def convertDateToBinary(self, date: str) -> str:
#         l_date = date.split("-")
#         bin_date = []
#         for num in l_date:
#             bin_date.append(bin(int(num))[2:])
#         return "-".join(bin_date)