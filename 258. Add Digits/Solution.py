class Solution:
    def addDigits(self, num: int) -> int:
        digit_root = 0
        while num > 0:
            digit_root += num % 10
            num //= 10

            if num == 0 and digit_root > 9:
                num = digit_root
                digit_root = 0
        return digit_root