class Book():
    author = ""
    title = ""
    publisher = ""
    date = ""


Book.author = "김씨"
Book.title = "파이썬시작하기"
Book.publisher = "김북스"
Book.date = "2021-09-16"

print(Book.author)  # 김씨
print(Book.title)  # 파이썬시작하기
print(Book.publisher)  # 김북스
print(Book.date)  # 2021-09-16


class Book():
    author = ""
    title = ""
    publisher = ""
    date = ""


book = Book()
# book은 Book클래스의 인스턴스
book.author = "김씨"
book.title = "파이썬시작하기"
book.publisher = "김북스"
book.date = "2021-09-16"

print(book.author)  # 김씨
print(book.title)  # 파이썬시작하기
print(book.publisher)  # 김북스
print(book.date)  # 2021-09-16
