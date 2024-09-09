class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = int("".join(reversed(str(num))))
        reversed2 = int("".join(reversed(str(reversed1))))
        if num == reversed2:
            return True
        return False