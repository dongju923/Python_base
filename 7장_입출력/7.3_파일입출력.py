### 파일 입력 ###
score_file = open("score.txt", "w", encoding="utf8")
# open()함수를 이용해서 파일을 열수있음, 단 파일이 없을경우 새로 생성
# score.txt 파일을 w(쓰기모드)로 열고 인코딩은 utf8로 설정(현재 파일이 없으므로 새로 생성후 열게됨)
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
# 파일에 쓰기
score_file.close()
# 파일 닫기

score_file = open("score.txt", "a", encoding="utf8")
# score.txt 파일을 a(추가모드)로 열고 인코딩은 utf8로 설정(현재 파일이 있으므로 생성없이 열기)
score_file.write("과학: 80\n")
score_file.write("영어: 100\n")
# write()함수로 쓸경우 자동으로 줄바꿈이 되지 않음
score_file.close()


### 파일 출력 ###
# 내용 한번에 출력
score_file = open("score.txt", "r", encoding="utf8")
# score.txt 파일을 r(읽기모드)로 열고 인코딩은 utf8로 설정
print(score_file.read())
score_file.close()


# 내용 한 줄씩 출력
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
# 한줄씩 읽고 커서(포인터)를 다음으로 옮김
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()


# 반복문을 이용한 출력
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:  # 더이상 출력할 줄이 없을때
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 내용물을 리스트 형태로 저장
for line in lines:  # 리스트 내용을 반복문으로 빼냄
    print(line, end="")
score_file.close()
