# O(dividend/divisor)

def func1(dividend, divisor):

    if (dividend < 0) ^ (divisor < 0):
        sign = -1
    else:
        sign = 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1

    if sign == -1:
        quotient = -quotient

    return quotient
