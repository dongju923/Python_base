# 리스트: 순서를 가지는 객체의 집합
# [~,~,~,~]

### 리스트 ###
print([])  # []
print(type([]))  # <class 'list'>
print([1, 2, 3])  # [1, 2, 3]
print(["One", "Two", "Three"])  # ['One', 'Two', 'Three']
print([1, "One", 2, "Two", 3, "Three"])  # [1, 'One', 2, 'Two', 3, 'Three']
print([1, 2, 3, ["One", "Two", "Three"]])  # [1, 2, 3, ['One', 'Two', 'Three']]


### 리스트 인덱싱 ###
# 리스트의 각 위치에 해당하는 값에 접근하기 위해서 주소 개념의 숫자를 사용
list = [1, 2, 3, 4, 5]
print(list)
print(list[0])  # 1
print(list[1])  # 2
print(list[3])  # 4
print(list[-4])  # 2
print(list[-2])  # 4
print(list[-1])  # 5


### 중첩 리스트 인덱싱 ###
list = [1, 2, 3, ["One", "Two", "Three"]]
print(list)  # [1, 2, 3, ['One', 'Two', 'Three']]
print(list[2])  # 3
print(list[3])  # ['One', 'Two', 'Three']
print(list[3][0])  # One
print(list[3][2])  # Three
print(list[-1])  # ['One', 'Two', 'Three']
print(list[-1][1])  # Two
print(list[-1][-3])  # One


### 리스트 슬라이싱 ###
list = ["One", "Two", "Three", "Four"]
print(list)  # ['One', 'Two', 'Three', 'Four']
print(list[0:])  # ['One', 'Two', 'Three', 'Four']
print(list[1:3])  # ['Two', 'Three']
print(list[2:])  # ['Three', 'Four']
print(list[:3])  # ['One', 'Two', 'Three']
print(list[1:-1])  # ['Two', 'Three']
print(list[:-2])  # ['One', 'Two']
print(list[-4:-1])  # ['One', 'Two', 'Three']


### 중첩 리스트 슬라이싱 ###
list = [1, 2, 3, ["One", "Two", "Three", "Four"]]
print(list)  # [1, 2, 3, ['One', 'Two', 'Three']]
print(list[2:4])  # [3, ['One', 'Two', 'Three']]
print(list[3][2:])  # ['Three', 'Four']
print(list[3][1:-2])  # ['Two']
print(list[3][:2])  # ['One', 'Two']

### 리스트 연산자 ###
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print(list_1+list_2)  # [1, 2, 3, 4, 5, 6]
print(list_1*3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 리스트의 길이 구하는 함수
print(len(list_1))  # 3


### 리스트 수정 ###
list = ["One", "Two", "Three"]
list[0] = 1
print(list)  # [1, 'Two', 'Three']
list[1] = 2
print(list)  # [1, 2, 'Three']
list[2] = 3
print(list)  # [1, 2, 3]
