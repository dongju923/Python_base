# try, except문을 이용해 예외를 처리할 수 있음
# try문을 통해 예외 발생 가능한 코드에 정의
# except문을 이용해 예외 처리 방법을 정의

try:
    print(3/0)
except:
    print("Error")
# Error

# 에러 분류에 따른 except문
try:
    print(3/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
# ZeroDivisionError

try:
    print(noname + 3)
except NameError:
    print("NameError")
# NameError

"""try:
    print(noname + 3)
except ZeroDivisionError:
    print("NameError")"""
# 실제 에러는 NameError인데 except문에 다른에러를 처리하면 그대로 오류가남


# 에러 메시지가 포함된 except문
try:
    print(3/0)
except ZeroDivisionError as e:
    print(e)
# division by zero

try:
    print(hi + 3)
except NameError as e:
    print(e)
# name 'hi' is not defined
