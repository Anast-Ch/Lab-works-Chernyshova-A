class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info (self):
        print(f"Название книги: {self.title}. Автор книги: {self.author}. Год издания: {self.year}. ")

book1 = Book("Граф Монте-Кристо", "Александр Дюма", "1844")
book1.get_info()

