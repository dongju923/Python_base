# math 모듈안에 있는 모든 함수와 메서드를 사용가능
# 파이썬에는 여러가지 모듈들이 있는데 그중 math모듈은 산술 계산 함수들이 모여있다
from math import *

# 절댓값 함수   abs()
print(abs(-5))  # 5

# 제곱 함수  pow()
print(pow(4, 2))  # 4^2 = 4*4 = 16
print(pow(2, 3))  # 2^3 = 2*2*2 = 8

# 최댓값 함수    max()
print(max(5, 10, 20))  # 20

# 최소값 함수    min()
print(min(10, 5, 30))  # 5

# 반올림 함수    round()
print(round(3.14))  # 3
print(round(5.69))  # 6

# 버림 함수
print(floor(4.99))  # 4
print(floor(3.12))  # 3

# 올림 함수
print(ceil(3.15))  # 4

# 제곱근 함수
print(sqrt(16))  # 4
print(sqrt(25))  # 5

# 로그 함수
print(log(2))
print(log(100, 10))  # 밑이 10으로 하는 로그 100의 값을 반환
