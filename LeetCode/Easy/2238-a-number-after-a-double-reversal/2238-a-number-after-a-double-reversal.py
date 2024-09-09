class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])
        return num == reversed2

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = int("".join(reversed(str(num))))
        reversed2 = int("".join(reversed(str(reversed1))))
        if num == reversed2:
            return True
        return False