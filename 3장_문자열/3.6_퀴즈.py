# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성

# 예) http://naver.com
# 규칙1: http://부분은 제외 => naver.com
# 규칙2: 처음 나오는 점(.) 이후 부분은 제외 = >naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!" 로 구성
# 생성된 비밀번호 : nav51!


"""password_site = "http://naver.com"
password = password_site[7:]
password = password.split(".")
password = str(password[0][0:3]) + \
    str(len(password[0])) + str(password[0].count("e")) + "!"
print(password)"""


"""url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)"""
