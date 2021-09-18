# key:value로 이루어진 데이터
# 순서가 없는 데이터
# key를 통해 value를 얻음
# 동일한 키가 있을경우 덮어씀
# {key:value}

dic = {1: "One", 2: "Two", 3: "Three"}
print(dic)
print(dic[1])  # One
print(dic[2])  # Two
print(dic[3])  # Three
# print(dic[100])   #에러 출력. 디버깅 강제종료
# print(dic.get(100))  # None 출력


### 딕셔너리 요소 추가 ###
dic[4] = "Four"
print(dic)  # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
dic[5] = "Five"
print(dic)  # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

### 딕셔너리 요소 삭제 ###
del dic[4]
print(dic)  # {1: 'One', 2: 'Two', 3: 'Three', 5: 'Five'}
del dic[5]
print(dic)  # {1: 'One', 2: 'Two', 3: 'Three'}

# 문자열 key:value도 가능
dic = {"Number1": "One", "Number2": "Two", "Number3": "Three"}
