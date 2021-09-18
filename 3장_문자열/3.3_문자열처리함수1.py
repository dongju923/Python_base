python = "Python is Amazing"

# 전부 소문자
print(python.lower())  # python is amazing

# 전부 대문자
print(python.upper())  # PYTHON IS AMAZING

# 단어의 첫 문자들을 대문자
print(python.title())  # Python Is Amazing

# 문장의 첫 문자를 대문자
print(python.capitalize())  # Python is amazing

# 대문자 판별
print(python[0].isupper())  # True
print(python[3].isupper())  # False

# 소문자 판별
print(python[10].islower())  # False
print(python[11].islower())  # True

# 길이 반환
print(len(python))  # 17

# 문자열 치환
print(python.replace("Python", "Java"))  # Java is Amazing

# 특정 문자 개수확인
print(python.count("n"))  # 2
print(python.count("Python"))  # 1

# 특정 문자 인덱스 찾기(find)
print(python.find("o"))  # 4
print(python.find("i"))  # 7
# (찾는 문자열이 없을경우 -1반환)
print(python.find("l"))  # -1
# (i라는 문자를 8번째 인덱스부터 찾음)
print(python.find("i", 8))  # 14

# 특정 문자 인덱스 찾기(index)
print(python.index("o"))  # 4
# (찾는 문자열이 없을 경우 오류발생)
# print(python.index("l"))
print(python.index("i", 8))
# (i라는 문자를 8번째 인덱스부터 찾음)
