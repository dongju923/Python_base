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


class JSS:
    def __init__(self): 
        # __init__함수는 클래스를 호출하는 순간 실행되는 함수
        # 클래스에서 반드시 필요한 내용, 없어서는 안되는 내용이 들어감
        print("JSS 클래스 선언!")
    def show(self):
        print("show 실행!")

a = JSS()
# a는 JSS클래스의 인스턴스임. 
# JSS클래스를 호출하면 __init__함수만 실행됨.
a.show()
# show함수 호출

""" self변수
self는 클래스의 인스턴스를 가리키는 변수
a.show() 처럼 사용이 가능
"""
""" 객체와 인스턴스 
사실 같은 의미이긴하나 클래스와 연관지어 말할 때는 인스턴스 라고 함
a는 객체이고 a는 JSS클래스의 인스턴스임
"""

class JSS:
    def __init__(self):
        self.name = input("이름: ")
        self.age =  input("나이: ")
    def show(self):
        print("저의 이름은 {}이고, 나이는 {}세 입니다.".format(self.name, self.age))

a=JSS()
print(a.name)
print(a.age)
a.show()
