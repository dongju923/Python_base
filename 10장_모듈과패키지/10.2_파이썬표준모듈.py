# 파이썬에서 기본으로 내장된 유용한 속성과 함수들이 있음

import random as rd
# random모듈의 이름을 rd로 사용할 수 있음
import statistics
# 통계모듈(산술평균, 표준편차 등 )
import itertools
# 순열과 조합 모듈(곱집합, 순열, 조합 등)
import math
# 수학 모듈
from datetime import date
import time
# 운영체제가 제공하는 시간 기능을 파이썬에서 사용할 수 있도록 만들어진 모듈
import sys
print(sys.builtin_module_names)
# 내장모듈을 전부 보여줌
print(dir(__builtins__))
# 내장객체를 전부 보여줌


print(time)
# <module 'time' (built-in)>

now = time.gmtime(time.time())
print(now)
# time.struct_time(tm_year=2021, tm_mon=9, tm_mday=18, tm_hour=5, tm_min=17, tm_sec=44, tm_wday=5, tm_yday=261, tm_isdst=0

year = str(now.tm_year)
month = str(now.tm_mon)
day = str(now.tm_mday)
print(f"{year}년 {month}월 {day}일")
# 2021년 9월 18일

today = date.today()
print(today)  # 2021-09-18

weekday = date.today().weekday()
print(weekday)  # 5
# 요일을 리스트 형태로 반환

weekday = "월화수목금토일"[weekday]
print(weekday)  # 토

print(today, weekday + "요일")
# 2021-09-18 토요일

print(math.factorial(5))  # 120
print(math.gcd(12, 24))  # 12
print(math.pi)  # 3.141592653589793
print(math.floor(math.pi))  # 3
print(math.pow(2, 10))  # 1024.0
print(math.radians(180))  # 3.141592653589793
print(math.sin(math.radians(90)))  # 1.0
print(math.cos(math.radians(180)))  # -1.0

print(dir(itertools))
# itertools 내장객체 출력
print(dir(statistics))
# statistics 내장객체 출력
print(rd.random())
print(rd.randrange(0, 10, 2))
