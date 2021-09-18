# 댓글 추점 프로그램 만들기
# 1~20개의 댓글중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게됨

# 조건1: 댓글개수는 1~20
# 조건2: 모두 무작위로 추점
# 조건3: random 모듈의 shuffle 과 sample을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2,3,4]
# -- 축하합니다 --

# 리스트 만들기 꿀팁
users = range(1, 101)
users = list(users)
print(users)  # 1~100까지 리스트 생성
