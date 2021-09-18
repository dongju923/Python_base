# __init__()메서드를 이용한 클래스의 속성들을 초기화
class Book(object):
    count = 0

    def __init__(self, author, title, publisher, date):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        Book.count += 1

    def print_info(self):
        print("Author: ", self.author)
        print("Title: ", self.title)
        print("Publisher: ", self.publisher)
        print("Date: ", self.date)


book = Book("김씨", "python programming", "dlab", "2020")
book.print_info()
print("Nomber Of Books: ", str(Book.count))


# __str__() 메서드를 이용해서 인스턴스 출력

class Book(object):
    count = 0

    def __init__(self, author, title, publisher, date):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        Book.count += 1

    def __str__(self):
        return ("Author: " + self.author +
                "\nTitle: " + self.title +
                "\nPublisher: " + self.publisher +
                "\nDate: " + self.date)


book = Book("이씨", "python programming", "anlab", "2020")
print(book)
print("Nomber Of Books: ", str(Book.count))
