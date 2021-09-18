# 함수의()안에 매개변수를 추가할수 있음
# 매개변수에 접근하기 위해서는 함수를 호출할때 ()안에 인자를 넣어주면됨
def hello(name):
    print("Hello", name)


hello("ABC")
# dongju라는 매개변수에 "dongju"라는 인자를 넣음


def add(a, b):
    print("a+b =", a+b)


add(3, 5)
# a, b 매개변수에 3, 5를 넣음
# a=3, b=5 로 함수를 실행


def add(a, b):
    return a+b


print(add(5, 6))
# 반환값이 있을 경우에는 반환값이 출력


def deposit(balance, money):
    print("얼마 추가하시겠습니까? {0}원".format(money))
    print(f"현재 잔액은 {balance+money} 입니다.")
    return balance+money


deposit(1000, 2000)


def withdraw(balance, money):
    print(f"얼마 출금하시겠습니까? {money}원")
    if balance >= money:
        print(f"출금이 완료되었습니다. 현재 잔액: {balance-money}원")
        return balance-money
    else:
        print(f"출금이 완료되지 않았습니다. 현재 잔액은 {balance}원 입니다.")
        return balance


withdraw(2000, 1000)
withdraw(1000, 2000)
