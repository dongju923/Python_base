# 조건에 따라 반복을 실행하는 문장
### for 반복문 ###
# for A in B:
#   문장
# A를 B만큼 반복

print("대기번호: 1")
print("대기번호: 2")
print("대기번호: 3")
print("대기번호: 4")

# 리스트 요소 반복
for wating in [1, 2, 3, 4]:
    print(f"대기번호: {wating}")

# 튜플 요소 반복
for wating in (1, 2, 3, 4):
    print(f"대기번호: {wating}")

# 문자열 요소 반복
string = "ABCDE"
for i in string:
    print(i)

# range(초기값, 마지막값, 증가값)
for i in range(5):
    print(i)
for i in range(0, 5, 1):
    print(i)
for i in range(1, 10, 2):
    print(i)
for i in range(1, 10):
    print(i)

# 반복 range()
for i in range(1, 10):
    for j in range(1, 10):
        print(i, j)

# for _ in range():
# _는 특정값이 필요하지 않거나 사용되지 않는 값을 대체함
for _ in range(5):
    print("Hi")


### while 반복문 ###
# while (조건):
#   문장
# 조건만큼 반복
# for 문과 다르게 증감식이 필요함

i = 1
while (i <= 10):
    print(i)
    i = i+1

i = 1
sum = 0
while i <= 10:
    sum = sum+i
    i += 1
print(sum)  # 55

i = 1
while i < 10:
    i = i + 1
    j = 1
    while j < 10:
        print(i, j)
        j = j + 1

### break문 ###
# 조건문 종료
i = 0
while i < 100:
    print(i)
    if i == 10:
        break
    i += 1

for i in range(100):
    print(i)
    if i == 10:
        break

### countinue문 ###
# 반복 조건문으로 이동
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


### 리스트 내포 ###
# 리스트 안에 for문과 if문 사용
list = [1, 2, 3, 4, 5]
print([i*2 for i in list])  # [2, 4, 6, 8, 10]
# i를 리스트만큼 반복시킨 값을 *2
print([i*2 for i in range(10) if i % 2 == 0])  # [0, 4, 8, 12, 16]
# i를 10번 반복하고 i%2==0인 경우에만 *2
