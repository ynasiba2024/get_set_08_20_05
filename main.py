#7-masala
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.__pages = pages

    def get_pages(self):
        return self.__pages

    def add_pages(self, value):
        self.__pages += value
        print("Sahifalar qo'shildi")


b1 = Book("Python", 120)

print(b1.title)
print(b1.get_pages())

b1.add_pages(30)
print(b1.get_pages())
