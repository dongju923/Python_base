### 출력 ###
# sep= 키워드
print("Python", "Java")
# Python Java
print("Python", "Java", sep=", ")
# Python, Java
# sep= 키워드는 출력 사이에 ,를 넣어줌
print("Python", "Java", sep=" vs ")
# Python vs Java
print("Python", "Java", "C++", sep=" vs ")
# Python vs Java vs C++

#end= 키워드
print("Python", "Java", end="")
print("뭐가 더 좋은가요?")
# Python Java뭐가 더 좋은가요?
# end= 키워드는 다음 출력문까지 한줄에 이어서 출력
print("Python", "Java", sep="?", end="?")
print("뭐가 더 좋은가요?")
# Python?Java?뭐가 더 좋은가요?

# rjust(), ljust()
scores = {"수학": 0, "국어": 50, "영어": 100}  # 과목 점수 변수
for subject, score in scores.items():  # scores딕셔너리의 개수만큼 반복(키:값 쌍으로 가져옴)해서 subject(키), score(값) 변수에 저장
    print(subject.ljust(4), str(score).rjust(8), sep=":")
    # ljust(4)는 왼쪽으로 4만큼 공간을 주고 정렬
    # rjust(8)는 오른쪽으로 8만큼 공간을 주고 정렬

# zfill()
for i in range(1, 11):  # range만큼 반복한 값을 i에 저장
    print("번호 : "+str(i).zfill(3))
    # zfill(3)은 공간을 3칸 할당하고 빈 공간을 0으로 채움


### 입력 ###
# input()함수로 키보드를 이용해 사용자로부터 값을 입력받을수 있음
answer = input("아무값이나 입력하세요\n")
print(f"입력한 값은 {answer}입니다")
# input()으로 받는 모든 값은 str형태로 저장됨
