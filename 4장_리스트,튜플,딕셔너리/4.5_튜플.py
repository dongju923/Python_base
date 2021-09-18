# 리스트와는 다르게 내용 변경, 추가가 불가능
# 하나의 변수에 여러 값 할당 가능
# (~,~,~,~)로 표현

print(type(()))  # <class 'tuple'>
print((1, 2, 3))  # (1, 2, 3)
print(("One", "Two", "Three"))  # ('One', 'Two', 'Three')
print((1, 2, 3, ('One', 'Two', 'Three')))  # (1, 2, 3, ('One', 'Two', 'Three'))


### 튜플 인덱싱 ###
# 튜플의 각 위치에 해당하는 값에 접근하기 위해서 주소 개념의 숫자를 사용
tuple = ("One", "Two", "Three")
print(tuple[0])  # One
print(tuple[2])  # Three
print(tuple[-1])  # Three
# tuple[0] = "Hi"
# TypeError: 'tuple' object does not support item assignment
# 튜플은 아이템 할당을 지원하지 않는다 즉 수정불가

### 중첩 튜플 인덱싱 ###
# 튜플안에 튜플이 중접되어 있을 경우, 인덱스 접근방법
tuple = (1, 2, 3, ('One', 'Two', 'Three'))
print(tuple[1])  # 2
print(tuple[3])  # ('One', 'Two', 'Three')
print(tuple[3][0])  # One
print(tuple[3][-2])  # Two

### 튜플 슬라이싱 ###
tuple = ('One', 'Two', 'Three', "Four")
print(tuple[0:])  # ('One', 'Two', 'Three', 'Four')
print(tuple[1:3])  # ('Two', 'Three')
print(tuple[1:-1])  # ('Two', 'Three')
print(tuple[-4:-2])  # ('One', 'Two')

### 중첩 튜플 슬라이싱 ###
tuple = (1, 2, 3, ('One', 'Two', 'Three'))
print(tuple[:3])  # (1, 2, 3)
print(tuple[2:])  # (3, ('One', 'Two', 'Three'))
print(tuple[3][1:])  # ('Two', 'Three')
print(tuple[3][:-1])  # ('One', 'Two')

### 튜플 연산자/함수 ###
tuple_1 = ('one', 'Two', 'Three')
tuple_2 = ('four', 'five', 'six')
print(tuple_1+tuple_2)  # ('one', 'Two', 'Three', 'four', 'five', 'six')
print(tuple_1*2)  # ('one', 'Two', 'Three', 'one', 'Two', 'Three')
print(len(tuple_1))  # 3
