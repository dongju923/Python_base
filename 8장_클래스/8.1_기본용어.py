### 클래스 ###
# 객체를 표현하기 위한 문법
# class 클래스이름:
#   내용

class abc():
    print("Hello")


abc()  # Hello

### 메서드 ###
# 클래스 안에 들어있는 함수
# 메서드의 첫 번째 매개변수는 반드시 self지정


class Person():
    def greeting(self):
        print("Hello")

### 인스턴스 ###
# 클래스는 특정 개념을 표현할 뿐 사용하려면 인스턴스를 생성해야함
# 인스턴스 = 클래스()


class Person():
    def greeting(self):
        print("Hello")


james = Person()
# james가 Person의 인스턴스임
james.greeting()  # Hello
# 메서드는 클래스가 아니라 인스턴스를 통해 호출함

### 객체와 인스턴스 ###
# 사실 같은 의미이긴하나 클래스와 연관지어 말할 때는 인스턴스 라고 함
# james는 객체이다
# james는 Person클래스의 인스턴스이다.
