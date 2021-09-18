# 변수란 어떤 데이터를 저장할 공간
# 변수명은 사용자가 지정가능하고 원하는 데이터를 대입가능
# 변수명 = 데이터
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3  # age가 3보다 크거나 같으면 is_adult변수는 True반환

print("우리집" + animal + "의 이름은" + name + "입니다")
print(name + "는" + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# 그냥 age로 사용할수 없는 이유: 문자열에서 + age + 로 사용할 수 없기 때문에 str()함수를 이용해 정수를 문자열로 변환시킴
print(name + "는 어른일까요?" + str(is_adult))
# 그냥 is_adult로 사용할수 없는 이유: 문자열에서 + is_adult + 로 사용할 수 없기 때문에 str()함수를 이용해 boolean을 문자열로 변환시킴

print("우리집", animal, "의 이름은", name, "입니다")
print(name, "는", age, "살이며,", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요?", is_adult)
# 문자열을 연결할 때 +대신 ,를 사용하면 문자열 변환필요없이 변수 사용가능
