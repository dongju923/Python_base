### append() ###
# 리스트 요소 추가
list = ["One", "Two", "Three"]
list.append("Four")
print(list)  # ['One', 'Two', 'Three', 'Four']
list.append("Five")
print(list)  # ['One', 'Two', 'Three', 'Four', 'Five']
list.append([1, 2, 3, 4, 5])
print(list)  # ['One', 'Two', 'Three', 'Four', 'Five', [1, 2, 3, 4, 5]]

### sort() ###
# 리스트 정렬
list = [30, 10, 40, 20]
list.sort()
print(list)  # [10, 20, 30, 40]
list = ["banana", "strawberry", "cherry", "apple"]
list.sort()
print(list)  # ['apple', 'banana', 'cherry', 'strawberry']

### reverse() ###
# 리스트 요소 반전
list = [1, 2, 3, 4, 5]
list.reverse()
print(list)  # [5, 4, 3, 2, 1]

### index() ###
# 리스트 요소 값에 대한 인덱스를 반환
list = [10, 40, 20, 30]
print(list.index(10))  # 0
print(list.index(20))  # 2
print(list.index(30))  # 3
print(list.index(40))  # 1

### insert() ###
# 리스트 요소 삽입
# insert(인덱스값, 삽입값)
list = [10, 40, 20, 30]
list.insert(4, 50)
print(list)  # [10, 40, 20, 30, 50]
list.insert(2, "3번째")
print(list)  # [10, 40, '3번째', 20, 30, 50]

### remove() ###
# 리스트 요소 제거
list = [10, 40, 20, 30, "안녕"]
list.remove(40)
print(list)  # [10, 20, 30, '안녕']
list.remove(10)
print(list)  # [20, 30, '안녕']
list.remove("안녕")
print(list)  # [20, 30]

### del ###
# 인덱스 제거 연산
list = [10, 40, 20, 30]
del list[0]
print(list)  # [40, 20, 30]
del list[2]
print(list)  # [40, 20]
print(list[0])  # 40

### pop() ###
# 리스트 요소를 방출
list = [10, 40, 20, 30]
list.pop()
print(list)  # [10, 40, 20]
list.pop(0)  # 0번 인덱스 값 방출
print(list)  # [40, 20]
print(list[0])  # 40
print(list[1])  # 20

### count() ###
# 리스트 요소의 갯수 계산
list = [10, 10, 20, 30, 30, 30]
print(list.count(30))  # 3
print(list.count(20))  # 1
print(list.count(0))  # 0

### extend() ###
# 리스트 확장
list_1 = [1, 2, 3]
list_2 = [4, 5]
list_1.extend(list_2)
print(list_1)  # [1, 2, 3, 4, 5]
list_1.extend([6, 7])
print(list_1)  # [1, 2, 3, 4, 5, 6, 7]
