sentence = "       Hello, World          "

# 문자열의 좌우 공백을 없앰
print(sentence.strip())

# 문자열의 오른쪽 공백을 없앰
print(sentence.rstrip())

# 문자열의 왼쪽 공백을 없앰
print(sentence.lstrip())

# split()함수는 list형식으로 반환

# 공백 기준으로 문자열 분리
print(sentence.split())

# ", " 기준으로 문자열 분리
print(sentence.split(", "))

# 좌우 공백을 모두없애고 ", " 기준으로 문자열 분리
print(sentence.strip().split(", "))
