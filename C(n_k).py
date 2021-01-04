from math import factorial
def C (n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    else:
        return 0

p10 = 0.3
p9 = 0.4
p8 = 0.2
p7 = 0.05
p6 = 0.05

test = C(5,1)
x = 2
y = x**2
first = (C(5,4) * p10**4 * (1 - p10)**1) * (C(5,1) * p7 * (1 - p7)**4)
second = (C(5,3) * p9 ** 3 * (1 - p9)**2) * (C(5,2) * p10**2 * (1 - p10)**3)
third = (C(5,3) * p10**3 * (1 - p10)**3 ) * (C(5,1) * p9 * (1 - p9)**4) * (C(5,1) * p8 * (1 - p8)**4)
total = first + second + third

answerF = factorial(5)/(factorial(4)* factorial(1)) * p10**4 * p7
answerS = factorial(5)/(factorial(3) * factorial(2)) * p10**2 * p9**3
answerT = factorial(5)/(factorial(3) * 1 * 1) * (p10**3 * p9 * p8)

asnwer = answerT + answerF + answerS
p = 100
p = 200