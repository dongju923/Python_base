# 변수는 유효한 범위가 존재
# 함수 안에서 선언된 변수는 함수 내부에서 유효함


def var_scope(a):
    a = a+1  # 1번 a


a = 10  # 2번 a
var_scope(a)
print(a)    # a = 10
# 1번 a와 2번 a는 서로 다른 변수


# 전역변수
a = 10  # 전역변수


def func1():
    a = 20  # 지역변수
    print(a)  # 지역변수의 a


func1()  # 20


def func2():
    print(a)  # 전역변수의 a


func2()  # 10

# global 키워드
# 함수 내부에서 전역변수를 사용하기 위한 키워드
a = 10


def func1():
    global a  # 전역변수 a
    a = 20  # 전역변수 a에 20으로 초기화
    print(a)  # 20


def func2():
    print(a)  # 20(위에서 전역변수 20으로 초기화)


func1()
func2()
