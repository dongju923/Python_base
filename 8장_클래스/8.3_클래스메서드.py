# 클래스 안에 있는 함수를 클래스 메서드라고함
# self가 있어야만 실제로 인스턴스가 사용할 수 있는 메서드로 선언
# self는 실제적으로 생성되는 인스턴스를 의미
# 메서드 안에서 속성 값을 사용하지 않을 경우에는 self 생략가능

# 메서드 안에서 속성 값을 사용한 경우
# self는 book인스턴스 자체를 의미한다
# self를 사용하면 인스턴스를 생성해야함
class Book():
    author = ""
    title = ""
    publisher = ""
    date = ""

    def print_book(self):
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("publisher: ", self.publisher)
        print("date: ", self.date)


book = Book()
book.author = "김씨"  # Author:  김씨
book.title = "파이썬시작하기"  # Title:  파이썬시작하기
book.publisher = "김북스"  # publisher:  김북스
book.date = "2021-09-16"  # date:  2021-09-16
book.print_book()


# 메서드 안에서 속성값을 사용하지 않은 경우
class Book():
    author = ""
    title = ""
    publisher = ""
    date = ""

    def print_book():
        print("Author: ", Book.author)
        print("Title: ", Book.title)
        print("publisher: ", Book.publisher)
        print("date: ", Book.date)


Book.author = "김씨"  # Author:  김씨
Book.title = "파이썬시작하기"  # Title:  파이썬시작하기
Book.publisher = "김북스"  # publisher:  김북스
Book.date = "2021-09-16"  # date:  2021-09-16
Book.print_book()
# 클래스 메서드 호출


class Book(object):
    author = ""
    title = ""
    publisher = ""
    date = ""

    def print_info(self):
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("Publisher: ", self.publisher)
        print("Date: ", self.date)

### 인스턴스 속성과 클래스 속성 ###
# 인스턴스 속성: 인스턴스를 통해 접근하는 속성
# 클래스 속성: 클래스를 통해 접근하는 속성


class Book():
    author = ""
    title = ""
    publisher = ""
    date = ""
    count = 0

    def print_book(self):
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("Publisher: ", self.publisher)
        print("Date: ", self.date)


book = Book()
book.author = "김씨"  # Author:  김씨
book.title = "파이썬시작하기"  # Title:  파이썬시작하기
book.publisher = "김북스"  # publisher:  김북스
book.date = "2021-09-16"  # date:  2021-09-16
# 인스턴스 속성
book.print_book()
Book.count = 1
# 클래스 속성
print("책 개수: ", Book.count)
