# 산술연산자
# 덧셈
print(1+1)  # 2
# 뺄셈
print(5-3)  # 2
# 곱셈
print(8*3)  # 24
# 나눗셈
print(6/3)  # 2
# 제곱
print(2**3)  # 8
# 나머지연산
print(5 % 3)  # 2
# 몫 연산
print(5//3)  # 1

# 관계연산자
print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # True
print(6 > 5 > 4)  # True
print(6 > 5 > 7)  # False

# 같다 ==
print(3 == 3)  # True
print(3+4 == 7)  # True
print("3" == 3)  # False

# 같지않다 (!=, not)
print(1 != 3)  # True
print(2 != 2)  # False
print(3 != "3")  # True
print(not(1 != 3))  # False

# 논리연산자
# 두 조건식 중 둘다 참이면 참 (and, &)
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (5 < 3))  # False
# 두 조건식 중 하나만 참이면 참 (or, |)
print((3 > 0) or (5 < 3))  # True
print((3 < 0) | (5 < 3))  # False

# 멤버연산자
# 포함 여부를 판단하는 연산자
list = [1, 3, 5, 7]
print(1 in list)  # True
print(2 in list)  # False
print(2 not in list)  # True

# 아이디 연산자
# 동일한 각체 여부를 판별하는 연산자
print(1 is 1)  # True
print("1" is 1)  # False
print(1 is not 2)  # True
print("1" is not 1)  # True
