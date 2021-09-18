### 내부 함수 ###
# 함수안에 함수가 존재하는 구조
# 내부 함수는 외부에서 호출 불가

def func1(a, b):
    def func2(num1, num2):
        return num1+num2
    return func2(a, b)


print(func1(5, 8))  # 13
# func1함수의 매개변수에 5, 8 저장
# func2함수의 매개변수에 a,b 즉 5, 8 저장
# 5+8 값을 반환
# func2(a,b)를 반환


### 재귀함수 ###
# 함수가 자기 자신을 다시 부르는 함수
def count(n):
    if n >= 1:
        print(n, end="")  # end=""는 줄바꿈을 하지않고 값을 옆으로 출력
        count(n-1)
    else:
        pass


count(10)  # 10987654321


def sum(n):
    if n == 1:
        return n
    else:
        return n + sum(n-1)


print(sum(10))  # 55


def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)


print(fact(5))  # 120


### 람다 함수 ###
# 함수를 한 줄로 간결하게 만들어서 사용


#add2 = lambda n1,n2:n1+n2
# print(add(6,4))

def add2(n1, n2):
    return n1+n2


print(add2(6, 4))
# 위와 똑같음


#add3 = lambda n1=9,n2=11: n1+n2
# print(add3())

def add3(n1=9, n2=11): return n1+n2


print(add3())
# 위와 똑같음
