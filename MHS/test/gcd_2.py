import math

# 두 수의 최대공약수를 구하는 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 세 개의 수의 최대공약수를 구하는 함수
def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)

# 사탕, 초콜릿, 젤리 개수
candies = 60
chocolates = 100
jellies = 80

# 최대공약수 계산
result = gcd_three(candies, chocolates, jellies)
print(result)