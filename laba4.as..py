#1 - Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами: имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password).
class UserAccount:
#2 - Используйте конструктор __init__ для инициализации этих атрибутов.
    def __init__(self, username, password, email):
        self.username = username
        self.__password = password
        self.email = email

# 3 - Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта
    def set_password(self, new_password):
        if self.check_password(new_password):
            print("Пароль совпадает!")
        else:
            self.__password = new_password

# 4 - Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль текущему паролю аккаунта и возвращает True или False.
    def check_password(self, password):
        return password == self.__password

#5 - Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его с помощью методов set_password и check_password.
user_account = UserAccount("Student", "k4rmar1ss", "student@mtuci.ru")
user_account.set_password("k4rmar1ss")
user_account.set_password("new_password")

#6 - Определите базовый класс Vehicle с атрибутами: make (марка) и model (модель), а также методом get_info(), который возвращает информацию о транспортном средстве.
class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

#7 - Создайте класс Car, наследующий от Vehicle, и добавьте в него атрибут fuel_type (тип топлива)
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.__fuel_type = fuel_type

#Переопределите метод get_info() таким образом, чтобы он включал информацию о типе топлива

    def get_info(self):
        print(f"Make: {self._make} Model: {self._model} Fuel type: {self.__fuel_type}")

vehicle = Vehicle("Volkswagen", "Golf VII")
vehicle.get_info()

car = Car("Audi", "R8", "Petrol")
car.get_info()
