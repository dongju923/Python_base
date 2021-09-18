sentence = "안녕하세요."

# 문자열 인덱스는 0부터 시작
print(sentence[0])  # 안
print(sentence[1])  # 녕
print(sentence[2])  # 하
print(sentence[3])  # 세
print(sentence[4])  # 요
print(sentence[5])  # .

# 인덱스의 처음부터 n번째 까지 출력
print(sentence[:6])  # 안녕하세요.
print(sentence[:4])  # 안녕하세

# 인덱스의 부분 출력
print(sentence[0:2])  # 안녕
print(sentence[2:6])  # 하세요.

# 인덱스의 n번째 부터 마지막까지 출력
print(sentence[0:])  # 안녕하세요.
print(sentence[2:])  # 하세요.

# 음수 인덱싱
print(sentence[-1])  # .
print(sentence[-2])  # 요
print(sentence[-3])  # 세
print(sentence[-4])  # 하
print(sentence[-5])  # 녕
print(sentence[-6])  # 안

# 음수인덱스 부분출력
print(sentence[1:-2])  # 녕하세
