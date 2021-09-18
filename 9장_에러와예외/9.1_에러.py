# (10/0)
# ZeroDivisionError: division by zero
# 0으로 나눌수 없음

#noname + 3
# NameError: name 'noname' is not defined
# noname이 정의되지 않음

# '1'+1
# TypeError: can only concatenate str (not "int") to str
# 문자열과 정수는 계산할 수 없음

# int("string")
# ValueError: invalid literal for int() with base 10: 'string'
# 문자열을 int형으로 변환할 수 없음


### raise문을 이용해 직접적으로 에러를 발생시킬 수 있음 ###

# raise ZeroDivisionError("숫자를 0으로 나눔")
# ZeroDivisionError: 숫자를 0으로 나눔


# raise NameError("지역 또는 전역 변수를 찾을 수 없음")
# NameError: 지역 또는 전역 변수를 찾을 수 없음
