import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        op = 1 if divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0  
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1 
        quotient = quotient  * op

        return math.trunc(quotient)


# print(Solution.divide("",10,3))
print(Solution.divide("",7,-3))