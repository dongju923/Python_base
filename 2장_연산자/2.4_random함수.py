# random모듈안에 있는 모든 메서드와 함수들을 사용
from random import *

# 0.0 ~ 1.0 미만의 난수 생성
print(random())

# 0.0 ~ 10.0 미만의 난수 생성
print(random()*10)

# 0 ~ 10 미만의 정수 난수 생성
print(int(random()*10))

# 1 ~ 10 이하의 정수 난수 생성
print(int(random()*10)+1)

# 1 ~ 46 미만의 난수 생성
print(randrange(1, 46))
