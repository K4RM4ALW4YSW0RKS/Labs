#1.1 - Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
class Book:
    title = ""

    author = ""

    year = ""

    def get_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

#1.2 - Добавьте метод get_info(), который возвращает информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]"
book = Book()
book.author = "Эдгар Аллан По"
book.title = "Падение дома Ашеров"
book.year = "1839"
book.get_info()

#2.1 - Определите класс Circle для представления круга
class Circle:
#2.2 - Используйте конструктор __init__ для инициализации радиуса круга (radius).
    def __init__(self, radius):
        self._radius = radius
#2.3 - Добавьте метод get_radius(), который возвращает значение радиуса.
    def get_radius(self):
        return self.__radius
#2.4 - Добавьте метод set_radius(new_radius), который позволяет изменить радиус круга.
    def set_radius(self, new_radius):
        self.__radius = new_radius

#2.5 - Создайте объект класса Circle, измените его радиус и выведите новый радиус на экран
circle = Circle(2)
circle.set_radius(8)
new_radius = circle.get_radius()
print(f"Radius: {new_radius}")

