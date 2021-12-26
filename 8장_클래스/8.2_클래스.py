### 클래스 상속 ###

class JSS:
    def __init__(self):
        self.name = input("이름: ")
        self.age =  input("나이: ")
    def show(self):
        print("저의 이름은 {}이고, 나이는 {}세 입니다.".format(self.name, self.age))

class JSS2(JSS):
    def __init__(self):
        super().__init__()
        # super함수는 부모 클래스의 __init__()을 가리키는 변수
        # 즉 JSS클래스의 __init__()을 가리키는 변수임
        self.gender = input("성별: ")
    def show(self):
        print("저의 이름은 {}, 성별은 {}자, 나이는 {}세 입니다.".format(self.name, self.gender, self.age))

a = JSS2()
a.show()