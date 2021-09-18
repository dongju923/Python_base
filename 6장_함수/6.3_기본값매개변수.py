# 함수의 매개변수에는 기본값을 설정할 수 있다
def profile(name, age=20, country="서울"):
    print(f"이름:{name}\t 나이: {age}\t 사는곳: {country}")


profile("김씨")
profile("한씨")


"""def profile(name, age=20, country):
    print(f"이름:{name}\t 나이: {age}\t 사는곳: {country}")

profile()"""
# 기본값 매개변수는 항상 맨 뒤에 있어야 한다.


def profile(name, country,  age=23,):
    print(f"이름:{name}\t 나이: {age}\t 사는곳: {country}")


profile("박씨", "서울")
profile("이씨", "부산")
