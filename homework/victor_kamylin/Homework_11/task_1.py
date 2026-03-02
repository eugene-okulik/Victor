class Library:
    page_material = "бумага"
    presence_of_text = True

    def __init__(self, title, author, count_pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserved = reserved

    def book_info(self):
        res = f"Название: {self.title}, Автор: {self.author}, "
        f"страниц: {self.count_pages}, материал: {self.page_material}"
        if self.reserved:
            return res + ", зарезервирована"
        return res


class Textbook(Library):
    def __init__(
        self, title, author, count_pages, isbn, item, school_class, task, reserved=False
    ):
        super().__init__(title, author, count_pages, isbn, reserved)
        self.item = item
        self.school_class = school_class
        self.task = task

    def textbook_info(self):
        res = f"Название: {self.title}, Автор: {self.author}, "
        f"страниц: {self.count_pages}, предмет: {self.item}, класс: {self.school_class}"
        if self.reserved:
            return res + ", зарезервирована"
        return res


print(Library("Война и мир", "Лев Толстой", 1225, "001").book_info())
print(Library("Колобок", "Народ", 3, "002").book_info())
print(Library("Преступление и наказание", "Достоевский", 352, "003").book_info())
print(Library("1984", "Оруэлл", 250, "001").book_info())
print(Library("Обитаемый остров", "Стругацкий", 200, "005", True).book_info())
print()
print(Textbook('Алгебра', 'Лимитов', 185, '011', 'Математика', '9', True).textbook_info())
print(Textbook('Химия', 'Водородов', 155, '015', 'Химия', '11', False).textbook_info())
print(Textbook('Правописание', 'Правилов', 125, '014', 'Русский язык', '1', True).textbook_info())
print(Textbook('Право', 'Лютый', 188, '0119', 'Обществознание', '8', False, True).textbook_info())
print(Textbook('География', 'Материков', 196, '016', 'География', '6', True).textbook_info())
