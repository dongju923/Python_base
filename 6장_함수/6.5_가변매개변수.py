# 매개변수가 몇 개인지 알 수 없을 때 사용
# 매개변수 앞에 * 을 표시
# 추후에 매개변수를 추가하거나 인자를 추가할 필요가 없음

"""def profile(name, age, fav_food1, fav_food2, fav_food3, fav_food4):
    print(
        f"이름:{name}, 나이:{age}, 좋아하는음식:{fav_food1},{fav_food2},{fav_food3},{fav_food4}")


profile("김씨", 23, "김치", "피자", "치킨", "떡볶이")
profile("이씨", 20, "피자", "치킨")"""
# 매개변수는 4개를 할당했는데 2개밖에 사용안하므로 오류


def profile(name, age, *fav_food):
    print(
        f"이름:{name}, 나이:{age}, 좋아하는음식:{fav_food}")


profile("김씨", 23, "김치", "피자", "치킨", "떡볶이")
profile("이씨", 20, "피자", "치킨")


def sum(*num):
    result = 0
    for i in num:  # 입력된 인자 수 만큼 반복
        result = result + i
    return result


print(sum(1, 2, 3))
print(sum(10, 50, 70))


### 가변키워드매개변수 ###
# 인자의 이름을 따로 지정하지 않고 사용
# 매개변수 앞에 **을 표시
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=5, b=8, n1=6, n2=2)
# 딕셔너리 형식으로 출력
