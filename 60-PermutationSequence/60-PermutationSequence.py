from math import factorial

class Solution:
    def getPermutation(self, n: int, position: int) -> str:
        position -= 1
        digits = list(range(1,n+1))
        result = ''
        digit = n - 1
        while digit > 0:
            chunk_size = factorial(digit)
            result += str(digits.pop(position // chunk_size))
            position = position % chunk_size
            digit -= 1
        return result + str(digits[0])