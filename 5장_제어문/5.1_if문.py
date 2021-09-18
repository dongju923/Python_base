# 조건에 따라 실행을 제어하는 문장
# if 조건:
#    실행문


### if문 ###
weather = "맑음"
if weather == "맑음":
    print("오늘 날씨는 맑아요")
# 오늘 날씨는 맑아요


### if-else문 ###
weather = "비"
if weather == "맑음":
    print("오늘 날씨는 맑아요")
else:
    print("오늘 날씨는 비가와요")
# 오늘 날씨는 비가와요


### if-elif-else문 ###
pm = 35
if pm < 16:
    print("미세먼지 농도: 좋음")
elif pm < 36:
    print("미세먼지 농도: 보통")
elif pm < 75:
    print("미세먼지 농도: 나쁨")
else:
    print("미세먼지 농도: 매우나쁨")
# 미세먼지 농도: 보통

temp = 25
if 35 <= temp:
    print("위험")
elif 10 <= temp and temp < 34:
    print("좋음")
else:
    print("추움")
# 좋음

### 중첩 if문 ###
pm = 80
if pm < 36:
    if pm < 16:
        print("미세먼지 농도: 좋음")
    else:
        print("미세먼지 농도: 보통")
else:
    if pm < 76:
        print("미세먼지 농도: 나쁨")
    else:
        print("미세먼지 농도: 매우나쁨")
# 미세먼지 농도: 매우나쁨


### if-pass문 ###
# 조건문은 있지만 실행할 문장이 없는경우, 오류가 발생하지 않도록 무시하고 넘어가는 기능
if 10 < 5:
    print("참")
else:
    pass


### if조건연산자 ###
# 비교 연산자
if 2 > 1:
    print("True")  # True
if 3 == 3:
    print("True")  # True
if 1 != 2:
    print("False")  # False
if 2 >= 1:
    print("Ture")  # True

# 논리 연산자(and, or, not)
rain = True
snow = True
sun = True

if rain and snow:
    print("진눈깨비")  # 진눈깨비
if rain or snow:
    print("눈 또는 비")  # 눈 또는 비
if not sun:
    print("흐림")
else:
    print("맑음")  # 맑음

# 멤버 연산자(in, not in)
list = ["One", "Two", "Three"]
if "One" in list:
    print("One")  # One
if "Four" not in list:
    print("No")  # No

# 식별 연산자(is, is not)
if "One" is "One":
    print("One")  # One
if "One" is not "Two":
    print("One is not Two")  # One is not Two


### 조건부 표현식 ###
# 한 라인으로 조건식을 사용한 표현
score = 75
msg = "통과" if score >= 70 else "탈락"
print(msg)
