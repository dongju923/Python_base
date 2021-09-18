# 내장되어있는 함수
# import따로 하지 않아도 사용이 가능
# dir() : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# 내장함수 목록 -> https://docs.python.org/ko/3/library/functions.html

import random
# print(dir())
# print(dir(__annotations__))
# print(dir(random))

name = "jin"
print(dir(name))
# name이라는 객체가 사용가능한 모든 함수, 메서드를 보여줌
