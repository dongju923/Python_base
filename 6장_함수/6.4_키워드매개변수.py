# 인자에 직접 값을 설정할 수 있음

def keyword(a, b, c):
    print(a, b, c)


keyword(b=2, c=5, a=8)
keyword(c=1, b=6, a=10)


def keyword(a, b, c):
    print("a+b+c = {0}".format(a+b+c))
    return a+b+c


keyword(b=2, c=5, a=8)
keyword(c=1, b=6, a=10)
