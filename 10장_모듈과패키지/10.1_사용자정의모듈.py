# 사용자가 사용할 모듈을 직접 정의
# 모듈 이름으로 파일명을 사용

"""import Practice_module
# 사용자가 직접 정의한 모듈을 import함

Practice_module.func1()  # 1번 함수
Practice_module.func2()  # 2번 함수
Practice_module.func3()  # 3번 함수"""

"""from Practice_module import *
# 사용자가 직접 정의한 Practice_module 모듈로부터 모듈안의 메서드를 모두 import함

func1()  # 1번 함수
func2()  # 2번 함수
func3()  # 3번 함수"""


"""from Calculator_module import *

print(add(3, 5))  # 8
print(sub(3, 5))  # -2
print(mul(3, 5))  # 15
print(div(3, 5))  # 0.6
print(mod(3, 5))  # 3"""
