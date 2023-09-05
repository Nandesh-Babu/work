import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor < 0 and dividend < 0:
            op = 1 
        elif divisor < 0 or dividend < 0:
            op = -1
        else:
            op = 1
        quotient = 0  
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend==1 and divisor==1:
            quotient = 1
            return math.trunc(quotient * op) 
        elif divisor == 1:
            return dividend * op
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1 
        quotient = quotient  * op

        return math.trunc(quotient)


# print(Solution.divide("",10,3))
print(Solution.divide("",7,-3))