def add(p1, p2):
    max_len = max(len(p1), len(p2))
    result = [0] * max_len
    for i in range(max_len):
        coef1 = p1[i] if i < len(p1) else 0
        coef2 = p2[i] if i < len(p2) else 0
        result[i] = coef1+coef2
    return polynomial(result)

def sub(p1, p2):
    max_len = max(len(p1), len(p2))
    result = [0]*max_len
    for i in range(max_len):
        coef1 = p1[i] if i < len(p1) else 0
        coef2 = p2[i] if i < len(p2) else 0
        result[i] = coef1-coef2
    return polynomial(result)

def mul(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i, coef1 in enumerate(p1):
        for j, coef2 in enumerate(p2):
            result[i + j] += coef1 * coef2
    return polynomial(result)

def div(p1, p2):
    divisor = len(p2)- 1
    dividend = p1[:]
    result = [0] * (len(dividend)-divisor)
    for i in range(len(dividend)-divisor):
        result[i] = dividend[i] / p2[0]
        for j in range(divisor+1):
            dividend[i + j] -= result[i] * p2[j]
    remainder = dividend[-divisor:]
    return polynomial(result), polynomial(remainder)

def derive(p):
    result = [coef*(len(p)-i - 1)
        for i,coef in enumerate(p[:-1])]
    return polynomial(result)

def integrate(p):
    result = [coef/(i + 1) for i,coef in enumerate(p)]
    return polynomial(result)